#include <iostream>
#include "Puzzle.hpp"

using namespace std;

int main(int ac, char **av) {
    
    if (ac == 2)
    {
        Puzzle puzzle = Puzzle(av[1]);
    }
    else
    {
        cout << "invalid number of argument";
    }
    return (0);
}
