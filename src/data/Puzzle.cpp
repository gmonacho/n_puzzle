#include "Puzzle.hpp"

#include <iostream>
#include <fstream>

#include "parsing/Parser.hpp"

Puzzle::Puzzle(std::string puzzlePath)
{
    fpp::Parser parser = fpp::Parser(puzzlePath);

    while (!parser.endOfFile())
    {
        this->grid.push_back(parser.getLineToVectorInt());
    }
    // std::cout << this->grid << std::endl; // TODO : libfpp fonction d'affichage (utiliser les templates?) 
}

