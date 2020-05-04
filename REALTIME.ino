#include <SimpleDHT.h>
int A =5;
int B=6;
int ValueA=0;
int ValueB=0;
int currentStateCLKA;
int previousStateCLKA;
int currentStateCLKB;
int previousStateCLKB;
int pinDHT11 = 3;
SimpleDHT11 dht11(pinDHT11);
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(A,INPUT);
pinMode(B,INPUT);
byte temperature = 0;
byte humidity = 0;
int err = SimpleDHTErrSuccess;

previousStateCLKA=digitalRead(A);
previousStateCLKB=digitalRead(B);

}

void loop() {
currentStateCLKA=digitalRead(A);
currentStateCLKB=digitalRead(B);
ValueA=digitalRead(A);
ValueB=digitalRead(B);


if (currentStateCLKA!=previousStateCLKA) 
{
//Serial.print("Direction: ");
//Serial.print(encdir);
//Serial.print("---Value ");

//Serial.println("ValueA : ");

Serial.print(ValueA);
//Serial.print(str);
Serial.print(ValueB);
//Serial.print(" ");
byte temperature;
byte humidity;
dht11.read(&temperature, &humidity, NULL);
Serial.print((int)temperature); 
Serial.println((int)humidity);
  
//Serial.println("ValueB : ");
//Serial.println("\n");
delay(1);

}
previousStateCLKA=currentStateCLKA;
previousStateCLKB=currentStateCLKB;


  delay(150);
}


  
