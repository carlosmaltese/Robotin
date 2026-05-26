#include <Arduino.h>
#include "protocol.h"
#include "servo_controller.h"
#include "sound_direction.h"

String inputLine;

void setup() {
  Serial.begin(115200);
  initServoController();
  initSoundDirection();
  Serial.println("EVT HEAD READY");
}

void loop() {
  while (Serial.available() > 0) {
    char c = static_cast<char>(Serial.read());
    if (c == '\n') {
      inputLine.trim();
      Serial.println(isKnownHeadCommand(inputLine) ? "OK" : "ERR unknown command");
      inputLine = "";
    } else if (c != '\r') {
      inputLine += c;
    }
  }
}

