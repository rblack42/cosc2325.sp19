#include <avr/io.h>

int state = 1;
char ticks = 0;

void toggleLED(void);

int main(void) {
    DDRB = (1 << 5);        // set pin 5 to output
    TIMSK0 = 0;             // no interrupts
    TCCR0B = 5;             // divide clock by 1024

    while(1) {
        while((TIFR0 & 0x01) == 0) {}    // loop until flag is set

        TIFR0 = 1;              // clear the flag
        ticks++;
        if(ticks == 60) {
            ticks = 0;
            toggleLED();
        }
    }
}

void toggleLED(void) {
    if(state == 1) {
        PORTB = 0;
        state = 0;
    } else {
        PORTB = (1 << 5);
        state = 1;
    }
}

        
