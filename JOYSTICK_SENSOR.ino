#define Pin_X A0
#define Pin_Y A1
int sw=2;
void setup() {
  Serial.begin(9600);    //Serial initializing 
  pinMode(Pin_X,INPUT);
  pinMode(Pin_Y,INPUT);
  digitalWrite(sw,HIGH);
}

void loop() {
  int sensorValueX = analogRead(Pin_X);      //X-axis input 
  int sensorValueY = analogRead(Pin_Y);      //Y-axis input 
  int swval=digitalRead(sw);
  //Serial.print("ValueX:");
  int data[] = {sensorValueX,sensorValueY,swval};
    //Serial.print("[");
    float sensorValueX1=sensorValueX/1024*5.0;
   float  sensorValueY1=sensorValueY/1024*5.0;
  Serial.print(sensorValueXM);
 Serial.print(",");
  //Serial.print("ValueY:");
  Serial.print(sensorValueY);
  //Serial.print("SW Value:");
      Serial.print(",");

  Serial.print(swval);
  Serial.println(" ");
   //Serial.print(",");

  delay(500);
}
