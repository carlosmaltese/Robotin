#include <Arduino.h>
#include "protocol.h"
#include "motor_driver.h"
#include "ramp_controller.h"
#include "safety.h"

String inputLine;

void setup() {
  Serial.begin(115200);
  initMotorDriver();
  initRampController();
  initMotorSafety();
  Serial.println("EVT MOTOR READY");
}

void loop() {
  while (Serial.available() > 0) {
    char c = static_cast<char>(Serial.read());
    if (c == '\n') {
      inputLine.trim();
      Serial.println(isKnownMotorCommand(inputLine) ? "OK" : "ERR unknown command");
      inputLine = "";
    } else if (c != '\r') {
      inputLine += c;
    }
  }
}

