#include <iostream>
int main(void) {
    char c;
    int count = 0;
    while(std::cin.get(c)) {
        if(c == '\n') break;
        count++;
    }
    std::cout << count << " charaters entered" << std::endl;
}
