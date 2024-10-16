// Code
#include <Ps3Controller.h>

const int voltagePin = 25;
int battery = 0;
void setup() {
  Serial.begin(115200);
  Serial2.begin(9600);
  Ps3.begin("1a:2b:3c:4d:5e:6f");
  Serial.println("Ready.");
  pinMode(14, OUTPUT);
  pinMode(voltagePin, INPUT);
}
void BatteryCharge() {
  if (battery != Ps3.data.status.battery) {
    battery = Ps3.data.status.battery;

    if (battery == ps3_status_battery_full) Ps3.setPlayer(4);
    else if (battery == ps3_status_battery_high)
      Ps3.setPlayer(3);
    else if (battery == ps3_status_battery_low)
      Ps3.setPlayer(2);
    else if (battery == ps3_status_battery_dying) Ps3.setPlayer(1);
    else if (battery == ps3_status_battery_shutdown) Ps3.setPlayer(0);
  }
}
int light = 0;
void loop() {
  if (Ps3.isConnected()) {
    BatteryCharge();
    if (Ps3.data.button.down) {
      Serial2.print("d");
    }
    if (Ps3.data.button.left) {
      Serial2.print("l");
    }
    if (Ps3.data.button.up) {
      Serial2.print("u");
    }
    if (Ps3.data.button.right) {
      Serial2.print("r");
    }
    if (Ps3.data.button.square) {
      Serial2.print("q");
    }
    if (Ps3.data.button.circle) {
      Serial2.print("m");
    }
    if (Ps3.data.button.triangle) {
      Serial2.print("t");
    }
    if (Ps3.data.button.cross) {
      Serial2.print("w");
    }
    if (Ps3.data.button.l1) {
      Serial2.print("k");
    }
    if (Ps3.data.button.r1) {
      Serial2.print("h")
    }
    if (Ps3.data.button.l2) {
      Serial2.print("b");
    }
    if (Ps3.data.button.r2) {
      Serial2.print("a");
    }
    if (Ps3.data.button.start) {
      Serial2.print("p");
    }
    if (Ps3.data.button.select) {
      Serial2.print("i");
    }
    if (Ps3.data.button.triangle && Ps3.data.button.r2) {
      Serial2.print("g");
    }
  }
}