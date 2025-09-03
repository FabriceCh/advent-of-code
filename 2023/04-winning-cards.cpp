#include <iostream>
#include "cppUtils/stringTheory.cpp"
#include <numeric>

using namespace std;

int problem()
{
    vector<string> ar = readInput();
    vector<int> cardsAmount(ar.size(), 1);
    cout << "starting part2" << endl;
    for (int c = 0; c < ar.size(); c++)

    {
        string line = ar[c];
        string all_numbers = stringSplit(line, ':')[1];
        string winningNumbersStr = stringSplit(all_numbers, '|')[0];
        string actualNumbersStr = stringSplit(all_numbers, '|')[1];
        int nWinningNumbers = 0;

        vector<int> winningNumbers;
        vector<int> actualNumbers;
        for (string const &num : stringSplit(winningNumbersStr, ' '))
        {
            winningNumbers.push_back(stoi(num));
        }
        for (string const &num : stringSplit(actualNumbersStr, ' '))
        {
            actualNumbers.push_back(stoi(num));
        }

        for (int i = 0; i < winningNumbers.size(); i++)
        {
            for (int j = 0; j < actualNumbers.size(); j++)
            {
                if (winningNumbers[i] == actualNumbers[j])
                {
                    nWinningNumbers += 1;
                }
            }
        }
        for (int cardInstancenWinnings = 1; cardInstancenWinnings <= nWinningNumbers; cardInstancenWinnings++)
        {
            cardsAmount[c + cardInstancenWinnings] += cardsAmount[c];
        }
    }
    cout << "total: " << accumulate(cardsAmount.begin(), cardsAmount.end(), 0) << endl;
    return 0;
}

int problem1()
{
    vector<string> ar = readInput();
    int total = 0;
    for (int i = 0; i < ar.size(); i++)
    {
        string line = ar[i];
        string all_numbers = stringSplit(line, ':')[1];
        string winningNumbersStr = stringSplit(all_numbers, '|')[0];
        string actualNumbersStr = stringSplit(all_numbers, '|')[1];
        int points = 0;

        vector<int> winningNumbers;
        vector<int> actualNumbers;
        for (string const &num : stringSplit(winningNumbersStr, ' '))
        {
            winningNumbers.push_back(stoi(num));
        }
        for (string const &num : stringSplit(actualNumbersStr, ' '))
        {
            actualNumbers.push_back(stoi(num));
        }

        for (int i = 0; i < winningNumbers.size(); i++)
        {
            for (int j = 0; j < actualNumbers.size(); j++)
            {
                if (winningNumbers[i] == actualNumbers[j])
                {
                    if (points == 0)
                    {
                        points = 1;
                    }
                    else
                    {
                        points *= 2;
                    }
                }
            }
        }
        total += points;
    }
    cout << "total: " << total << endl;
    return 0;
}