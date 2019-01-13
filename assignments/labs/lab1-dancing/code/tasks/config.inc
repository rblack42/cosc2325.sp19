; config.inc - pin assignments for this project

#include <avr/io.h>

#define     LED_PORT   PORTD
#define     LED_DIR    DDRD
#define     LED_PIN    6

#define     BUZZ_PORT  PORTB
#define     BUZZ_DIR   DDRB
#define     BUZZ_PIN1  4
#define     BUZZ_PIN2  5

#define     PULSE_DIR  DDRD
#define     PULSE_PORT PORTD
#define     PULSE_PIN  7
