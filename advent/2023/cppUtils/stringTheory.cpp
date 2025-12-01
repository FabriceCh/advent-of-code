#include <string>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

vector<string> readInput(string inputFileName = "input")
{
    vector<string> ar;

    string line;
    ifstream inputFile(inputFileName);
    while (getline(inputFile, line))
    {
        ar.push_back(line);
    }
    return ar;
}

vector<string> stringSplit(string inputString, char separator)
{
    string tmpstr;
    vector<string> strSplit;
    stringstream stream(inputString);

    while (getline(stream, tmpstr, separator))
    {
        if (tmpstr != "")
        {
            strSplit.push_back(tmpstr);
        }
    }
    return strSplit;
}