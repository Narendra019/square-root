
int A =5;
int B=6;
int state;
int counter=0;
int currentStateCLK;
int previousStateCLK;
String encdir="";    
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(A,INPUT);
previousStateCLK=digitalRead(A);

}

void loop() {
currentStateCLK=digitalRead(A);
counter=digitalRead(A);
if (currentStateCLK!=previousStateCLK)
{
//Serial.print("Direction: ");
//Serial.print(encdir);
//Serial.print("---Value ");
delay(200);
Serial.println(counter);
delay(1000);

}
previousStateCLK=currentStateCLK;



}
