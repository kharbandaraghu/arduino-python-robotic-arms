#include <Servo.h>
#include <Wire.h>
//#include <SoftwareSerial.h>

// create array for incoming bytes
int incoming[2];

// Create servo objects
Servo q; 
Servo w; 
Servo e; 
Servo r; 
Servo t; 



void setup() {
  // to monitor serial port
  Serial.begin(9600);
  // attatch servo to port
  q.attach(8);
  w.attach(9);
  e.attach(10);
  r.attach(11);
  t.attach(12);
  q.write(0);
  w.write(180);
  e.write(180);
  r.write(180);
  t.write(0);
  

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
    // send the first value as 255 to trigger, second arguement - is pin and the third one is incoming[2]s
        if (incoming[0] == 255)
        {
          if(incoming[1]==1){
              q.write(incoming[2]);
          }
          if(incoming[1]==2){
              w.write(incoming[2]);
          }
          if(incoming[1]==3){
              e.write(incoming[2]);
          }
          if(incoming[1]==4){
              r.write(incoming[2]);
          }
          if(incoming[1]==5){
              t.write(incoming[2]);
          }
          delay(20);
      }
  }


}
