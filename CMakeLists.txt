cmake_minimum_required(VERSION 3.0.0)
project(cmaketest VERSION 0.1.0 LANGUAGES C CXX)

set(HEADER_FILES /2023/cppUtils/node.h)
include(CTest)
enable_testing()

add_executable(cmaketest main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
