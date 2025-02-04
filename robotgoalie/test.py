import cv2 as cv
import numpy as np

img = cv.imread("InClass.png")
cam = cv.VideoCapture(0)

# get frame width and height
frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))


lower_orange_value = np.array([5, 150, 180])  # Darker neon orange (loosened S & V)
upper_orange_value = np.array([20, 255, 255])  # Brighter neon orange (increased S & V)

'''
# adjusted HSV range to account for lighting & distance changes
lower_orange_value = np.array([8, 150, 180])  # lowered S & V to detect dimmer shades
upper_orange_value = np.array([22, 255, 255])  # increased upper H to include orange variations
'''
'''
lower_orange_value_box = np.array([5, 180, 170])  # Allow slightly darker and less saturated orange
upper_orange_value_box = np.array([15, 255, 255])  # Ensure bright neon orange is captured
'''


while True:
    ret, frame = cam.read()

    if not ret:
        break
    
    # convert image to HSV 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower_orange_value, upper_orange_value)

    # apply morphological transformations to reduce noise
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    # find the contours in the image
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv.contourArea(contour) > 200:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2) # draw bounding box
            cv.putText(frame, "orange ball", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # show frames
    cv.imshow("live feed", frame)

    # write the frame to the output
    out.write(frame)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
out.release()
cv.destroyAllWindows()
