# Protocol

The initial protocol is plain text, one command per line, terminated by `\n`.

Examples:

```text
SYS HEARTBEAT
FACE STATUS
FACE EXPR happy
FACE LOOK left
FACE MOUTH talking
FACE BLINK
HEAD LOOK 15 -5
MOTOR DRIVE 0.2 0.2
MOTOR STOP
LIGHT MODE thinking
```

## FACE Initial Contract

The first real FACE implementation has two levels:

- Level A: serial firmware only, no real GC9A01 graphics.
- Level B: initialize one GC9A01, then two displays, then expressions.

Level A commands:

```text
SYS HEARTBEAT
FACE STATUS
FACE EXPR neutral
FACE EXPR happy
FACE EXPR sad
FACE EXPR angry
FACE EXPR curious
FACE LOOK center
FACE LOOK left
FACE LOOK right
FACE LOOK up
FACE LOOK down
FACE BLINK
FACE SLEEP
FACE WAKE
```

Expected FACE events and responses:

```text
EVT FACE READY
OK FACE <COMMAND>
ERR FACE UNKNOWN_COMMAND
ERR FACE INVALID_ARGS
EVT FACE STATUS expression=<expr> look=<look> awake=<0|1>
```

Examples:

```text
> FACE EXPR happy
< OK FACE EXPR
> FACE STATUS
< EVT FACE STATUS expression=happy look=center awake=1
```

## Response Style

Generic firmware skeletons may respond with:

```text
OK
ERR unknown command
```

Subsystem-specific firmware should prefer the more explicit `OK <SUBSYSTEM> <COMMAND>` and `ERR <SUBSYSTEM> <REASON>` forms.

Subsystems can emit events:

```text
EVT FACE READY
EVT MOTOR FAULT overcurrent
```

## Evolution to JSON Lines

When commands need richer payloads, the project can add JSON Lines without changing the transport:

```json
{"type":"command","subsystem":"FACE","action":"EXPR","args":{"name":"happy"}}
```

Plain text remains useful for manual debugging and bring-up.
