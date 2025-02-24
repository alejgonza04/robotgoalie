import serial
import time

# ✅ Use the correct serial port (check with ls /dev/ttyACM*)
SERIAL_PORT = "/dev/ttyACM0"  
BAUD_RATE = 115200

# ✅ Initialize serial connection
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # ✅ Give Arduino time to initialize

# ✅ Infinite loop: Alternate between RIGHT and LEFT
while True:
    arduino.write(b"RIGHT\n")  # Send RIGHT command
    arduino.flush()  # ✅ Ensure the message is sent completely
    print("✅ Sent: RIGHT")
    time.sleep(1)  # ✅ Wait 1 second

    arduino.write(b"LEFT\n")  # Send LEFT command
    arduino.flush()  # ✅ Ensure the message is sent completely
    print("✅ Sent: LEFT")
    time.sleep(1)  # ✅ Wait 1 second