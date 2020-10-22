#include <vector>

class Puzzle
{

private:

    std::vector<std::vector<int>> grid;

public:

    Puzzle(std::string puzzlePath);
    ~Puzzle() = default;

};