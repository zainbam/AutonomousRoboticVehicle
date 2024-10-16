// Code
#include <TomIBT2.h>

#include <NewPing.h>

#define man 48
#define RPWM1 12
#define LPWM1 13
#define R_EN1 52
#define L_EN1 53
#define RPWM2 4
#define LPWM2 5
#define R_EN2 34
#define L_EN2 35
#define RPWM3 7
#define LPWM3 6
#define R_EN3 32
#define L_EN3 33
#define RPWM4 11
#define LPWM4 10
#define R_EN4 25
#define L_EN4 24

#define RPWM5 9
#define LPWM5 8
#define R_EN5 27
#define L_EN5 26
#define FTrig 38
#define FEcho 39
#define RTrig 23
#define REcho 22
#define LTrig 38
#define LEcho 37
#define In1 29
#define In2 31
#define In3 30
#define In4 28
TomIBT2 motor1(R_EN1, L_EN1, RPWM1, LPWM1);
TomIBT2 motor2(R_EN2, L_EN2, RPWM2, LPWM2);
TomIBT2 motor3(R_EN3, L_EN3, RPWM3, LPWM3);
TomIBT2 motor4(R_EN4, L_EN4, RPWM4, LPWM4);
TomIBT2 motor5(R_EN5, L_EN5, RPWM5, LPWM5);
NewPing
Sonic[3] = {
  NewPing(FTrig, FEcho, 100),
  NewPing(RTrig, REcho, 100),
  NewPing(LTrig, LEcho, 100)
};
int FrontDistance = 40; //IN CM 
int RightDistance = 30;
int LeftDistance = 20;
int FrontUltra = 0;
int RightUltra = 1;
int LeftUltra = 2;

void setup() {
  motor1.begin();
  motor2.begin();
  motor3.begin();
  motor4.begin();
  motor5.begin();
  Serial.begin(9600);
  Serial3.begin(9600);
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  pinMode(In3, OUTPUT);
  pinMode(In4, OUTPUT);
  digitalWrite(In1, HIGH);
}
void StopMotors() {
  motor1.stop();
  motor2.stop();
  motor3.stop();
  motor4.stop();
}
void Straight(int speed1 = 255, int speed2 = 255) {
  motor1.rotate(speed1, TomIBT2::CW);
  motor2.rotate(speed2, TomIBT2::CW);
  motor3.rotate(speed2, TomIBT2::CW);
  motor4.rotate(speed1, TomIBT2::CW);
}
void Left(int speed1 = 255, int speed2 = 0) {
  motor1.rotate(speed1, TomIBT2::CW);
  motor2.rotate(speed2, TomIBT2::CW);
  motor3.rotate(speed2, TomIBT2::CW);
  motor4.rotate(speed1, TomIBT2::CW);
  digitalWrite(In2, HIGH);
}

void Right(int speed1 = 255, int speed2 = 0) {
  motor1.rotate(speed2, TomIBT2::CW);
  motor2.rotate(speed1, TomIBT2::CW);
  motor3.rotate(speed1, TomIBT2::CW);
  motor4.rotate(speed2, TomIBT2::CW);
  digitalWrite(In3, HIGH);
}
void Back(int speed = 255) {
  motor1.rotate(speed, TomIBT2::CCW);
  motor2.rotate(speed, TomIBT2::CCW);
  motor3.rotate(speed, TomIBT2::CCW);
  motor4.rotate(speed, TomIBT2::CCW);
  digitalWrite(In2, HIGH);
  digitalWrite(In3, HIGH);
}
void AntennaUp() {
  motor5.rotate(255, TomIBT2::CCW);
}
void AntennaDown() {
  motor5.rotate(255, TomIBT2::CW);
}
void UltrasonicFunc() {
  if (Sonic[FrontUltra].ping_cm() < FrontDistance) {
    Straight(127, 127);
    delay(10000);
  } else if (Sonic[RightUltra].ping_cm() < LeftDistance) {
    Left(255, 150);
    delay(3000);
  } else if (Sonic[LeftUltra].ping_cm() < RightDistance) {
    Right(255, 150);
    Serial.println("GOing Right");
  }
}

String RecieveData() {
  while (1) {
    if (Serial.available() > 0) {
      String recievedData = Serial.readString();
      return recievedData;
    }
  }
}
void JetsonCommand(String JetsonData = "DEFAULT") {
  if (JetsonData == "Straight") {
    Straight();
  } else if (JetsonData == "Back") {
    Back();
  } else if (JetsonData == "right") {
    Right();
  } else if (JetsonData == "left") {
    Left();
  } else if (JetsonData == "Stop") {
    StopMotors();
  }
}
void Ps3Command(char Ps3Flag) {
  if (Ps3Flag == 117) {
    Straight(255, 175);
    Serial.print('u');
  } else if (Ps3Flag == 100) {
    Back();
    Serial.print('d');
  } else if (Ps3Flag == 114) {
    Right(255, 100);
    Serial.print('r');
  } else if (Ps3Flag == 108) {
    Left(255, 100);
    Serial.print('l');
  } else if (Ps3Flag == 119) {
    StopMotors();
    
    Serial.print("Stop");
  }
}
int mFlag = 0;
void loop() {
  int Ps3Flag = Serial3.read();
  Serial.println(Ps3Flag);
  if (Ps3Flag == 109) {
    mFlag = 1;
  }
  if (Ps3Flag == 113) {
    mFlag = 0;
  }
  if (mFlag == 1) {
    Ps3Command(Ps3Flag);
  } else {
    digitalWrite(man, HIGH);
    String JetsonData = RecieveData();
    Serial.println(JetsonData);
    JetsonCommand(JetsonData);
  }
  //UltrasonicFunc(); 
  //Serial.println("Front: "+String(Sonic[FrontUltra].ping_cm())); 
  //Serial.println("Right: "+String(Sonic[RightUltra].ping_cm())); 
  //Serial.println("Left: "+String(Sonic[LeftUltra].ping_cm())); 
}