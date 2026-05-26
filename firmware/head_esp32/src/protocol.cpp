#include "protocol.h"

bool isKnownHeadCommand(const String& line) {
  return line.startsWith("HEAD LOOK ") ||
         line == "HEAD CENTER" ||
         line.startsWith("HEAD GESTURE ") ||
         line == "HEAD STATUS" ||
         line == "SYS HEARTBEAT";
}

