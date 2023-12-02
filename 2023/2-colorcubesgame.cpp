#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

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

bool isGamePossible(string rounds)
{
    int maxRed = 12;
    int maxGreen = 13;
    int maxBlue = 14;
    vector<string> roundsVec = stringSplit(rounds, ';');
    for (const string &round : roundsVec)
    {

        int totalRed, totalGreen, totalBlue;
        totalRed = totalGreen = totalBlue = 0;

        vector<string> pulls = stringSplit(round, ',');
        for (const string &pull : pulls)
        {
            vector<string> pullDetails = stringSplit(pull, ' ');
            int qty = stoi(pullDetails[0]);
            string color = pullDetails[1];
            if (color == "red")
            {
                totalRed += qty;
            }
            else if (color == "green")
            {
                totalGreen += qty;
            }
            else
            {
                totalBlue += qty;
            }
        }
        if (totalRed > maxRed || totalGreen > maxGreen || totalBlue > maxBlue)
        {
            return false;
        }
    }
    return true;
}

int part2GamePower(string rounds)
{
    int maxRed, maxGreen, maxBlue;
    maxRed = maxGreen = maxBlue = 0;
    vector<string> roundsVec = stringSplit(rounds, ';');
    for (const string &round : roundsVec)
    {

        int totalRed, totalGreen, totalBlue;
        totalRed = totalGreen = totalBlue = 0;

        vector<string> pulls = stringSplit(round, ',');
        for (const string &pull : pulls)
        {
            vector<string> pullDetails = stringSplit(pull, ' ');
            int qty = stoi(pullDetails[0]);
            string color = pullDetails[1];
            if (color == "red")
            {
                totalRed += qty;
            }
            else if (color == "green")
            {
                totalGreen += qty;
            }
            else
            {
                totalBlue += qty;
            }
        }
        if (totalRed > maxRed)
        {
            maxRed = totalRed;
        }
        if (totalGreen > maxGreen)
        {
            maxGreen = totalGreen;
        }
        if (totalBlue > maxBlue)
        {
            maxBlue = totalBlue;
        }
    }
    return maxBlue * maxRed * maxGreen;
}

int main()
{
    vector<string> ar;

    string line;
    ifstream inputFile("input");
    while (getline(inputFile, line))
    {
        ar.push_back(line);
    }

    int IdsSUm = 0;

    for (int i = 0; i < ar.size(); i++)
    {
        vector<string> gameRoundsSplit;
        gameRoundsSplit = stringSplit(ar[i], ':');
        string game = gameRoundsSplit[0];
        string rounds = gameRoundsSplit[1];
        int gameID = stoi(stringSplit(game, ' ')[1]);
        cout << gameID << endl;
        IdsSUm += part2GamePower(rounds);
    }

    cout << endl
         << IdsSUm << endl;
}
