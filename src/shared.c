#include "shared.h"

volatile LIN_State lin_state = LIN_STATE_WAIT_SYNC;
volatile uint8_t lin_buffer[5];
volatile uint8_t lin_pos = 0;