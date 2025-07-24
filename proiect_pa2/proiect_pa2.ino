#include <Servo.h>
Servo servo;

void setup() {
  servo.attach(4);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String j = Serial.readStringUntil('\n');
    j.trim();

    if (j == "deschide") {
      for (int p = 180; p >= 0; p -= 15) 
        servo.write(p);
        
      
    } else if (j == "inchide") {
      for (int p = 0; p <= 90; p += 15) {
        servo.write(p);
      }
    }
  }
}