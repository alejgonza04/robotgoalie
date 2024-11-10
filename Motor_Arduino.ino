#define BUTTON_PIN7 7  // The Arduino UNO R4 pin connected to the button
#define BUTTON_PIN4 4
#include <Servo.h>

Servo servo;  // Initialize a Servo object to manage a servo
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // initialize the pushbutton pin as a pull-up input
  pinMode(BUTTON_PIN7, INPUT_PULLUP);
  pinMode(BUTTON_PIN4, INPUT_PULLUP);
  servo.attach(5);  // Connects the servo on pin 9 to the servo object
  servo.write(0);   // Moves the servo to 0 degrees immediately upon startup
}

void loop() {
  // read the state of the switch/button:
  int button_state1 = digitalRead(BUTTON_PIN7);
  int button_state2 = digitalRead(BUTTON_PIN4);
  int counter_clockwise = 1;

  if (button_state1 == 0){
    
    for (int pos = 0; pos <= 180; pos += 1) {  // Gradually move the servo from 0 to 180 degrees
    servo.write(pos);  // Set servo position to 'pos' degrees
    if (pos == 180){
      pos = 0;
    }
    if (button_state1 == )         // Delay 10ms to allow the servo to reach the new position
  }
    counter_clockwise = 0;
    Serial.println("Button 1");
  }
  else if (button_state2 == 0){
    for (int pos = 180; pos >= 0; pos -= 1) {  // Gradually move the servo from 0 to 180 degrees
    servo.write(pos);  // Set servo position to 'pos' degrees
    if (pos == 0){
      pos = 180;
    }   
    Serial.println("Button 2");
  }
  }

  delay(100);
}
