#ifndef SHARED_H
#define SHARED_H

#include "stm32f1xx_hal.h"

typedef enum {
    LIN_STATE_WAIT_SYNC,
    LIN_STATE_WAIT_ID,
    LIN_STATE_RECEIVING_DATA
} LIN_State;

extern volatile LIN_State lin_state;
extern volatile uint8_t lin_buffer[5];
extern volatile uint8_t lin_pos;

#endif
