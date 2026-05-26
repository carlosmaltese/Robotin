#include <Arduino.h>
#include "protocol.h"
#include "display_driver.h"
#include "eye_renderer.h"

String inputLine;

void setup() {
  Serial.begin(115200);
  initDisplayDriver();
  initEyeRenderer();
  Serial.println("EVT FACE READY");
}

void loop() {
  while (Serial.available() > 0) {
    char c = static_cast<char>(Serial.read());
    if (c == '\n') {
      inputLine.trim();
      if (isKnownFaceCommand(inputLine)) {
        // TODO: Level A contract should respond with OK FACE <COMMAND>.
        Serial.println("OK");
      } else {
        // TODO: Level A contract should distinguish UNKNOWN_COMMAND and INVALID_ARGS.
        Serial.println("ERR unknown command");
      }
      inputLine = "";
    } else if (c != '\r') {
      inputLine += c;
    }
  }
}
