# Number of sectors to divide the screen into
num_sectors = 9  # Adjust based on how many divisions you want (e.g., 9 lines = 8 sectors)

# Calculate the width of each sector
sector_width = frame_width / num_sectors

# Find contours of the ball
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
if contours:
    # Get the largest contour (assuming it's the ball)
    largest_contour = max(contours, key=cv.contourArea)
    M = cv.moments(largest_contour)
    if M["m00"] > 0:
        # Calculate centroid of the ball
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        # Determine which sector the ball is in
        sector = int(cx // sector_width)

        # Send command to Arduino based on the sector
        command = f"SECTOR_{sector}\n"
        arduino.write(command.encode())
        print(f"sent to arduino: {command.strip()}")

        # Optional: Draw the centroid on the frame for debugging
        cv.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
