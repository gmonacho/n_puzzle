cmake_minimum_required(VERSION 3.10)

project(n_puzzle)

add_subdirectory("${PROJECT_SOURCE_DIR}/libfpp")

add_executable(${PROJECT_NAME}
    src/main.cpp
    src/data/Puzzle.cpp
)

# find_library(LIBFPP 
#     NAMES fpp
#     HINTS "${PROJECT_NAME}/libfpp/${CMAKE_BUILD_TYPE}"
# )

# message(STATUS "path: ${LIBFPP}")

target_link_libraries(${PROJECT_NAME} "${PROJECT_SOURCE_DIR}/libfpp/build/libfpp.a")

target_include_directories(${PROJECT_NAME} PRIVATE
    src/data
    libfpp/src
)

# include_directories()