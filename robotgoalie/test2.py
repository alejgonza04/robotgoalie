import cv2 as cv

img = cv.imread("InClass.png")
# convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blur the image to reduce the noise while thresholding
blur = cv.GaussianBlur(gray, (5, 5), 0)  # Larger kernel for better smoothing

#apply  thresholding to image
#using thresh_binary directly targets brihgt areas (whitespace) without inverting the colors
#high threshold value of 240 ensures only areas close to pure white are considered for contour detection
_, thresh = cv.threshold(blur, 240, 255, cv.THRESH_BINARY)

#find the contours in the image
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Filter and refine contours

#draw the obtained contour lines 
cv.drawContours(img, contours, -1, (0, 255, 0), 2)
cv.imshow('Contours', img)
k = cv.waitKey(0) # Wait for a keystroke in the window
