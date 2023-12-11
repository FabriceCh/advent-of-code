
#include <iostream>
#include <utility>
#include "cppUtils/stringTheory.cpp"
#include <numeric>
#include <chrono>

bool areAllOk(vector<int> &pass)
{
    int bi = pass[0];
    for (int ii : pass)
    {
        if (ii != bi)
        {
            return false;
        }
    }
    return true;
}

long long gcd(long long a, long long b)
{
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}

long long llcm(long long a, long long b)
{
    return (a * b) / gcd(a, b);
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
    vector<string> ar2 = {
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
    vector<int> firstPass, secondPass;

    for (string cu : cur)
    {
        int i = 0;
        int count = 0;
        while (cu[2] != 'Z')
        {
            if (instructions[i] == 'L')
            {
                cu = mapping[cu].first;
            }
            else
            {
                cu = mapping[cu].second;
            }
            i++;
            count++;
            i = i % instructions.size();
        }
        firstPass.push_back(count);
    }

    long long leastCommonMultiple = llcm(llcm(llcm(llcm(llcm(firstPass[0], firstPass[1]), firstPass[2]), firstPass[3]), firstPass[4]), firstPass[5]);

    cout << leastCommonMultiple << endl;
}