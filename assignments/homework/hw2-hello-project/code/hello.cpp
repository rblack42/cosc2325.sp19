#include <iostream>
#include <string>

void message(string name) {
    std::cout << "My name is " << name << std::endl;
}

int main(void) {
    std::string myname = "Roie R. Black";
    message(myname);
}

