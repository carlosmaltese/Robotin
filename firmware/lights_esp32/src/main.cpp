#include <Arduino.h>
#include "protocol.h"
#include "light_effects.h"

String inputLine;

void setup() {
  Serial.begin(115200);
  initLightEffects();
  Serial.println("EVT LIGHT READY");
}

void loop() {
  while (Serial.available() > 0) {
    char c = static_cast<char>(Serial.read());
    if (c == '\n') {
      inputLine.trim();
      Serial.println(isKnownLightCommand(inputLine) ? "OK" : "ERR unknown command");
      inputLine = "";
    } else if (c != '\r') {
      inputLine += c;
    }
  }
}

