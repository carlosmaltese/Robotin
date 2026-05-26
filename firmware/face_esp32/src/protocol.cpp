#include "protocol.h"

bool isKnownFaceCommand(const String& line) {
  return line == "FACE EXPR neutral" ||
         line == "FACE EXPR happy" ||
         line == "FACE EXPR sad" ||
         line == "FACE EXPR angry" ||
         line == "FACE EXPR curious" ||
         line == "FACE LOOK left" ||
         line == "FACE LOOK right" ||
         line == "FACE LOOK center" ||
         line == "FACE LOOK up" ||
         line == "FACE LOOK down" ||
         line == "FACE BLINK" ||
         line == "FACE SLEEP" ||
         line == "FACE WAKE" ||
         line == "FACE STATUS" ||
         line == "SYS HEARTBEAT";
}
