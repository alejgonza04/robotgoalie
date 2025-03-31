import cv2 as cv
import numpy as np
from picamera2 import Picamera2
import serial
import time

# Initialize serial communication with Arduino (update port accordingly)
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Change port to match Arduino
#time.sleep(2)  # Give Arduino time to initialize

# Initialize the PiCamera2
picam2 = Picamera2()

# Start the camera
picam2.start()

# Get the camera resolution (use the default resolution or set one)
frame_width = 320
frame_height = 240

# Video writer setup
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

'''
# Video writer setup
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))'''

lower_orange_value = np.array([5, 150, 180])  # Darker neon orange (loosened S & V)
upper_orange_value = np.array([20, 255, 255])  # Brighter neon orange (increased S & V)

AREA_THRESHOLD = 500

while True:
    frame = picam2.capture_array("main")

    # Resize and convert to HSV
    frame = cv.resize(frame, (frame_width, frame_height))
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create mask for orange color
    mask = cv.inRange(hsv, lower_orange_value, upper_orange_value)

    # Apply morphological transformations to reduce noise
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    command = None
    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        area = cv.contourArea(largest_contour)

        if area > AREA_THRESHOLD:
            x, y, w, h = cv.boundingRect(largest_contour)
            ball_center = x + w // 2
            
            # map ball position to servo
            angle = int((ball_center / frame_width) * 180)
            angle = max(0, min(180, angle))

            # send angle to Arduino
            arduino.write(f"{angle}\n".encode())
            arduino.flush()
            print(f"Sent angle: {angle}")

            time.sleep(0.1)

    cv.imshow("Live Feed", frame)
    #cv.imshow("Mask", mask)

#time.sleep(0.1) 
    # Break loop if 'q' is pressed
    if cv.waitKey(1) == ord('q'):
        break

picam2.stop()
arduino.close()
cv.destroyAllWindows()
