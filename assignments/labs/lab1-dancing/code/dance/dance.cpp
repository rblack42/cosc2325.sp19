#include <iostream>
#include <string>
#include <sstream>

// defaults
const int MAX_STEPS = 100;
const int MAX_DANCERS = 20;
const int INIT_STEPS = 10;
const int INIT_DANCERS = 5;
const int INIT_CARDS = 6;

// globals are UGLY!
int cards[MAX_DANCERS+1] = {0};
int nsteps = INIT_STEPS;
int ndancers = INIT_DANCERS;
int ncards = INIT_CARDS;
bool debug = false;
bool stable = false;

void usage() {
    std::cout << "Usage: " 
        << "dancer [-d] [-c cards] [-n dancers] [-s steps]"
        << std::endl;
    exit(1);
}

void show_cards() {
    // display the current cards
    for(int i=0;i<ndancers+1;i++)
        std::cout << cards[i] << " ";
    std::cout << std::endl;
}
 
std::string show_step(int d) {
    std::ostringstream out;
    out << "(" 
	    << cards[d] 
            << "," 
            << cards[d+1] 
            << ")";
    return out.str();
}

void arg_parse(int argc, char *argv[]) {
    // process input parameters    
    int i=1;
    while(true) {
        if(i>=argc) break;    
        if(argv[i][0] == '-')
            switch(argv[i][1]) {
            case 'c': ncards = std::stoi(argv[++i]); break;
            case 'n': ndancers = std::stoi(argv[++i]); break;
            case 's': nsteps = std::stoi(argv[++i]); break;
            case 'd': debug = true; break;
            default: usage();
        } else usage();
        i++; // look for next arg
    }
}

void dance_step(int dancer, int step) {
    // this dancer needs to get happy!
    if(debug) std::cout << "\tstep: " 
            << step << " dancer " 
            << dancer << std::endl;
    // show current cards
    if(debug) std::cout << "\t  " 
            << show_step(dancer) << " --> ";
    // balance the cards
    // show the final cards
    if(debug) std::cout << show_step(dancer) << std::endl;
}

int main(int argc, char *argv[]) {
    // say hello
    std::cout << "Dance-Cards (v0.1)" << std::endl;
    arg_parse(argc, argv);
    if(debug) {
        std::cout << ndancers 
            << " dancers will dance " 
	    << nsteps << " steps" << std::endl;
        std::cout << "Initial card count is " 
            << ncards << std::endl;
    }
    // let the music begin!
    if(debug) std::cout << "Let the dance begin!" << std::endl;
    cards[0] = ncards;
    show_cards();
    for(int step=0; step<nsteps; step++) {
        for(int dancer=0; dancer<ndancers; dancer++){
            dance_step(dancer, step);
        }
        if(stable) {
            std::cout << "system is stable" << std::endl;
            break;
        }
        show_cards();
    }
}
        
