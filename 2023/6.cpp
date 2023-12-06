#include <iostream>
#include "cppUtils/stringTheory.cpp"
#include <numeric>
#include <chrono>

using namespace std;

void problem1()
{
    // vector<string> ar = readInput();
    vector<int> times = {59, 70, 78, 78};
    vector<int> distances = {
        430,
        1218,
        1213,
        1276,
    };
    int acc = 1;
    for (int i = 0; i < 4; i++)
    {
        int n_ways = 0;
        int time = times[i];
        int dist = distances[i];
        for (int hold = 0; hold < time; hold++)
        {
            int score = hold * (time - hold);
            if (score > dist)
            {
                n_ways++;
            }
        }
        acc *= n_ways;
    }
    cout << acc << endl;
}

void problem()
{
    // part 1
    {
        std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
        problem1();
        std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();

        std::cout << "Part 1 Time = " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "[µs]" << std::endl;
    }
    // part 2
    {
        std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
        long time = 59707878;
        long distance = 430121812131276;
        long n_ways = 0;
        for (long hold = 0; hold < time; hold++)
        {
            long score = hold * (time - hold);
            if (score > distance)
            {
                n_ways++;
            }
        }
        std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
        cout << n_ways << endl;

        std::cout << "Part 2 Time difference = " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "[µs]" << std::endl;
    }
}
