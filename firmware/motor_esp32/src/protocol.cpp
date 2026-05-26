#include "protocol.h"

bool isKnownMotorCommand(const String& line) {
  return line.startsWith("MOTOR DRIVE ") ||
         line == "MOTOR STOP" ||
         line == "MOTOR STATUS" ||
         line == "SYS HEARTBEAT";
}

