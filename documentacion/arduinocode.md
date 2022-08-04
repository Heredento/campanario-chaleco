int analogValue = A0;
int ledPin = D8;
void setup() {
pinMode(analogValue, INPUT);
pinMode(ledPin, OUTPUT);
Serial.begin(115200);
}

void loop() {
  int readValue=analogRead(analogValue);
  Serial.print("Valor análogo: ");
  Serial.println(readValue);
  analogWrite(ledPin, readValue);
  delay(50);
}