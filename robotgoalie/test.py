import cv2 as cv
img = cv.imread("InClass.png")
cam = cv.VideoCapture(0)

# get frame width and height
frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()
    # convert image to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Blur the image to reduce noise (Gaussian Blur works better for circles)
    blur = cv.GaussianBlur(gray, (9, 9), 2)


    #app thresholding to image
    ret, thresh = cv.threshold(blur, 1, 255, cv.THRESH_OTSU)

    #find the contours in the image
    contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv.contourArea(contour) > 500:
            cv.drawContours(frame, [contour], -1, (0, 255, 0), 2)
    
    # show frames
    cv.imshow("live feed", frame)

    # write the frame to the output
    out.write(frame)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
out.release()
cv.destroyAllWindows()
