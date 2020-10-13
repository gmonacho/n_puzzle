cmake_minimum_required(VERSION 3.10)
project(n_puzzle)

set (CMAKE_C_FLAGS "-Wall -Wextra -Werror")

# include_directories()

add_executable(${PROJECT_NAME} 
srcs/main.cpp
srcs/Puzzle.cpp
)