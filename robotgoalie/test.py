import cv2 as cv
img = cv.imread("InClass.png")
# convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blur the image to reduce the noise while thresholding
blur = cv.blur(gray, (10, 10))

#app;u  thresholding to image
ret, thresh = cv.threshold(blur, 1, 255, cv.THRESH_OTSU)

#find the contours in the image
contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#draw the obtained contour lines 
cv.drawContours(img, contours, -1, (0, 244, 0), 20)
cv.namedWindow('Contours', cv.WINDOW_NORMAL)
cv.namedWindow('Thresh', cv.WINDOW_NORMAL)
cv.imshow('Contours', img)
cv.imshow('Thresh', thresh)
k = cv.waitKey(0) # Wait for a keystroke in the window