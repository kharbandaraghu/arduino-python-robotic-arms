#include <Servo.h>
#include <Wire.h>

// create array for incoming bytes
int incoming[2];

// Create servo objects
Servo CentreArm; // motor 1
Servo HeightLever; // motor 2
Servo Rotation; // motor 3
Servo Clipper; // motor 4

// setting min max ranges
  int m1_min = 65;
  int m1_max = 140;
  int m2_min = 80;
  int m2_max = 160;
  int m3_min = 2;
  int m3_max = 178;
  int m4_min = 90;
  int m4_max = 150;

void setup() {
  // to monitor serial port
  Serial.begin(9600);
  // attatch servo to port
  CentreArm.attach(8);
  HeightLever.attach(9);
  Rotation.attach(10);
  Clipper.attach(11);

  CentreArm.write(60); // 70 - 120
  HeightLever.write(90);
  Rotation.write(90);
  Clipper.write(150); // 88 - 155

  

}

// function to increment - controll with keyboard
void Alter(int motor, int degree) {
  if (motor == 1) {
    if (degree >= m1_min && degree <= m1_max ) {
      CentreArm.write(degree);
      
    }
  } else if (motor == 2) {
    if (degree >= m2_min && degree <= m2_max ) {
      HeightLever.write(degree);
    }
  } else if (motor == 3) {
    if (degree >= m3_min && degree <= m3_max ) {
      Rotation.write(degree);
    }
  } else if (motor == 4) {
    if (degree >= m4_min && degree <= m4_max ) {
      Clipper.write(degree);
    }
  }
}

// function to slowly set the position of the arm to the desired angle
void SetTo(int motor, int degree) {
  if (motor == 1) {
    int currentVal = CentreArm.read();
    if (currentVal > degree) {
      for (int i = currentVal; i > degree; --i) {
        CentreArm.write(i);
        delay(10);
      }
    } else {
      for (int i = currentVal; i < degree; ++i) {
        CentreArm.write(i);
        delay(10);
      }
    }
  } else if (motor == 2) {
    int currentVal = HeightLever.read();
    if (currentVal > degree) {
      for (int i = currentVal; i > degree; --i) {
        HeightLever.write(i);
        delay(10);
      }
    } else {
      for (int i = currentVal; i < degree; ++i) {
        HeightLever.write(i);
        delay(10);
      }
    }
  } else if (motor == 3) {
    int currentVal = Rotation.read();
    if (currentVal > degree) {
      for (int i = currentVal; i > degree; --i) {
        Rotation.write(i);
        delay(10);
      }
    } else {
      for (int i = currentVal; i < degree; ++i) {
        Rotation.write(i);
        delay(10);
      }
    }
  } else if (motor == 4) {
    int currentVal = Clipper.read();
    if (currentVal > degree) {
      for (int i = currentVal; i > degree; --i) {
        Clipper.write(i);
        delay(10);
      }
    } else {
      for (int i = currentVal; i < degree; ++i) {
        Clipper.write(i);
        delay(10);
      }
    }
  }
}

void loop() 
{
  if (Serial.available() >= 3) 
  {
    // get input bytes    
    for (int i = 0; i < 3; i++)
    {
      incoming[i] = Serial.read();
    }
    // send the first value as 255 to trigger, second arguement - is pin and the third one is degrees
    if (incoming[0] == 255)
    {
        Alter(incoming[1], incoming[2]); 
    }
  }
}