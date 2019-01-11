#include <avr/io.h>

int main(void) {

    char key = 0;
    char op = '+';
    char sum = 0;
    char y;

    while(1) {
        key = PORTB;;
        if(key == '+') op = '+';
        else if(key == '-') op = '-';
        else {
            y = (key - '0');
            while(y > 0) {
                if(op == '+') sum++;
                if(op == '-') sum--;
                y--;
            }
        }
        PORTC = sum;
    }
}

