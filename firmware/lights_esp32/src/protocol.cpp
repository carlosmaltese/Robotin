#include "protocol.h"

bool isKnownLightCommand(const String& line) {
  return line.startsWith("LIGHT MODE ") ||
         line == "LIGHT STATUS" ||
         line == "SYS HEARTBEAT";
}

