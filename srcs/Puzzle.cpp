#include <iostream>
#include <fstream>
#include <vector>
#include "Puzzle.hpp"

using namespace std;

Puzzle::Puzzle(string puzzlePaths)
{
    ifstream file;
    string line;

    file.open(puzzlePaths);
    while (!file.eof())
    {
        getline(file, line);
        // parse the line to pieces
        cout << line << '\n';
    }
}

