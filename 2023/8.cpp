
#include <iostream>
#include <utility>
#include "cppUtils/stringTheory.cpp"
#include <numeric>
#include <chrono>

bool areAllOk(vector<string> &cour)
{
    for (string cs : cour)
    {
        if (cs[2] != 'Z')
        {
            return false;
        }
    }
    return true;
}

void problem()
{
    vector<string> ar = readInput();

    // ar = {
    //    "LLR",
    //"",
    //"AAA BBB BBB",
    //"BBB AAA ZZZ",
    //"ZZZ ZZZ ZZZ"};
    ar = {
        "LR",

        "11A 11B XXX",
        "11B XXX 11Z",
        "11Z 11B XXX",
        "22A 22B XXX",
        "22B 22C 22C",
        "22C 22Z 22Z",
        "22Z 22B 22B",
        "XXX XXX XXX",
    };

    string instructions = ar[0];
    map<string, pair<string, string>> mapping;
    vector<string> cur;
    for (int i = 2; i < ar.size(); i++)
    {
        vector<string> a = stringSplit(ar[i], ' ');
        if (a[0][2] == 'A')
        {
            cur.push_back(a[0]);
        }
        pair<string, string> lr(a[1], a[2]);
        mapping.insert(pair<string, pair<string, string>>(a[0], lr));
    }
    int count = 0;
    int i = 0;
    while (!areAllOk(cur))
    {
        count++;
        for (int j = 0; j < cur.size(); j++)
        {
            if (instructions[i] == 'L')
            {
                cur[j] = mapping[cur[j]].first;
            }
            else
            {
                cur[j] = mapping[cur[j]].second;
            }
        }
    }
    cout << count << endl;
}