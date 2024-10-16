#include <SoftwareSerial.h>

SoftwareSerial bluetooth(10, 11); // RX, TX

#define RPWM1 5
#define LPWM1 6
#define R_EN1 3
#define L_EN1 4

#define RPWM2 9
#define LPWM2 8
#define R_EN2 7
#define L_EN2 2

#define RPWM3 11
#define LPWM3 12
#define R_EN3 A0
#define L_EN3 A1

#define RPWM4 13
#define LPWM4 14
#define R_EN4 A2
#define L_EN4 A3

void setup() {
  // Set motor connections as outputs
  pinMode(RPWM1, OUTPUT);
  pinMode(LPWM1, OUTPUT);
  pinMode(R_EN1, OUTPUT);
  pinMode(L_EN1, OUTPUT);

  pinMode(RPWM2, OUTPUT);
  pinMode(LPWM2, OUTPUT);
  pinMode(R_EN2, OUTPUT);
  pinMode(L_EN2, OUTPUT);

  pinMode(RPWM3, OUTPUT);
  pinMode(LPWM3, OUTPUT);
  pinMode(R_EN3, OUTPUT);
  pinMode(L_EN3, OUTPUT);

  pinMode(RPWM4, OUTPUT);
  pinMode(LPWM4, OUTPUT);
  pinMode(R_EN4, OUTPUT);
  pinMode(L_EN4, OUTPUT);

  // Bluetooth setup
  bluetooth.begin(9600);

  // Stop motors initially
  stopMotors();
}

void loop() {
  if (bluetooth.available() > 0) {
    char command = bluetooth.read();

    switch (command) {
      case 'F':
        moveForward();
        break;
      case 'B':
        moveBackward();
        break;
      case 'L':
        moveLeft();
        break;
      case 'R':
        moveRight();
        break;
      case 'S':
        stopMotors();
        break;
      case 'C':
        customControl(); // Added a new case for custom control
        break;
    }
  }
}

void moveForward() {
  setMotorSpeed(255, 255);
}

void moveBackward() {
  setMotorSpeed(-255, -255);
}

void moveLeft() {
  setMotorSpeed(64, 255); // 25% duty cycle for LPWM, 100% for RPWM
}

void moveRight() {
  setMotorSpeed(255, 64); // 100% duty cycle for LPWM, 25% for RPWM
}

void stopMotors() {
  setMotorSpeed(0, 0);
}

void customControl() {
  // Receive two characters for left and right speeds
  int leftSpeed = bluetooth.read() - '0'; // Convert ASCII to integer
  int rightSpeed = bluetooth.read() - '0';

  // Receive one character for direction
  char direction = bluetooth.read();

  // Convert direction to sign (-1 for reverse, 1 for forward)
  int directionSign = (direction == 'R') ? 1 : -1;

  // Adjust speeds based on direction and set motor speed
  setMotorSpeed(leftSpeed * directionSign, rightSpeed * directionSign);
}

void setMotorSpeed(int leftSpeed, int rightSpeed) {
  // Set direction pins
  digitalWrite(R_EN1, rightSpeed >= 0 ? HIGH : LOW);
  digitalWrite(L_EN1, leftSpeed >= 0 ? HIGH : LOW);
  
  digitalWrite(R_EN2, rightSpeed >= 0 ? HIGH : LOW);
  digitalWrite(L_EN2, leftSpeed >= 0 ? HIGH : LOW);

  digitalWrite(R_EN3, rightSpeed >= 0 ? HIGH : LOW);
  digitalWrite(L_EN3, leftSpeed >= 0 ? HIGH : LOW);

  digitalWrite(R_EN4, rightSpeed >= 0 ? HIGH : LOW);
  digitalWrite(L_EN4, leftSpeed >= 0 ? HIGH : LOW);

  // Set speed using PWM
  analogWrite(LPWM1, abs(leftSpeed));
  analogWrite(RPWM1, abs(leftSpeed));
  analogWrite(LPWM2, abs(rightSpeed));
  analogWrite(RPWM2, abs(rightSpeed));
  analogWrite(LPWM3, abs(leftSpeed));
  analogWrite(RPWM3, abs(leftSpeed));
  analogWrite(LPWM4, abs(rightSpeed));
  analogWrite(RPWM4, abs(rightSpeed));
}
