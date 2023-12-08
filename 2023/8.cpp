
#include <iostream>
#include <utility>
#include "cppUtils/stringTheory.cpp"
#include <numeric>
#include <chrono>

void problem()
{
    vector<string> ar = readInput();

    // ar = {
    //    "LLR",
    //"",
    //"AAA BBB BBB",
    //"BBB AAA ZZZ",
    //"ZZZ ZZZ ZZZ"};
    string instructions = ar[0];
    map<string, pair<string, string>> mapping;
    for (int i = 2; i < ar.size(); i++)
    {
        vector<string> a = stringSplit(ar[i], ' ');
        pair<string, string> lr(a[1], a[2]);
        mapping.insert(pair<string, pair<string, string>>(a[0], lr));
    }
    string current = "AAA";
    int count = 0;
    int i = 0;
    while (current != "ZZZ")
    {
        count++;

        if (instructions[i] == 'L')
        {
            current = mapping[current].first;
        }
        else
        {
            current = mapping[current].second;
        }
        i = (i + 1) % instructions.size();
    }
    cout << count << endl;
}