#define BUTTON_PIN7 7  // The Arduino UNO R4 pin connected to the button
#define BUTTON_PIN4 4
#include <Servo.h>

Servo servo;  // Initialize a Servo object to manage a servo
int position = 90;  // Start at center (90°)
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  servo.attach(5);  // Connects the servo on pin 9 to the servo object
  servo.write(0);   // Moves the servo to 0 degrees immediately upon startup
  Serial.println("Enter a value:");
}

void loop() {
  // read the state of the switch/button:
  int button_state1 = digitalRead(BUTTON_PIN7);
  int button_state2 = digitalRead(BUTTON_PIN4);
  int counter_clockwise = 1;
    
    if (Serial.available() > 0) {  // Check if data is available
      String input = Serial.readStringUntil('\n');  // Read input until newline
      input.trim();

      int angle = input.toInt();

      // check for valid angle
      if (angle >= 0 && angle <= 180) {
      servo.write(angle);  // Move servo to the specified angle
      position = angle;
      Serial.print("Moved to angle: ");
      Serial.println(angle);
    } else {
      Serial.print("Invalid input: ");
      Serial.println(input);
      }
    }

  delay(100);

}
