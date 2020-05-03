
int A =5;
int B=6;
int ValueA=0;
int ValueB=0;
int currentStateCLKA;
int previousStateCLKA;
int currentStateCLKB;
int previousStateCLKB;
String encdir="";    
String str = ",";

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(A,INPUT);
previousStateCLKA=digitalRead(A);
previousStateCLKB=digitalRead(B);

}

void loop() {
currentStateCLKA=digitalRead(A);
currentStateCLKB=digitalRead(A);

ValueA=digitalRead(A);
ValueB=digitalRead(B);
if ((currentStateCLKA!=previousStateCLKA) && (currentStateCLKB!=previousStateCLKB))
{
//Serial.print("Direction: ");
//Serial.print(encdir);
//Serial.print("---Value ");

//Serial.println("ValueA : ");

Serial.print(ValueA);
//Serial.print(str);
Serial.println(ValueB);

//Serial.println("ValueB : ");
//Serial.println("\n");
delay(1000);

}
previousStateCLKA=currentStateCLKA;
previousStateCLKB=currentStateCLKB;


}
