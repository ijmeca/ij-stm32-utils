#include "linUtils.h"
#include "stdio.h"
#include <stdbool.h>
#include <stdint.h>
#include <string.h>



void delay_us(uint32_t us) {
    uint32_t startTick = DWT->CYCCNT;
    uint32_t ticks = us * (SystemCoreClock / 1000000);
    while ((DWT->CYCCNT - startTick) < ticks);
}

