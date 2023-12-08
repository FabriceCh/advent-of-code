#include <iostream>
#include <utility>
#include "cppUtils/stringTheory.cpp"
#include <numeric>
#include <chrono>

using namespace std;

bool isNumberInMapValues(map<int, int> m, int v)
{
    for (auto x : m)
    {
        if (x.second == v)
        {
            return true;
        }
    }
    return false;
}

class Hand
{
private:
    int cards[5];
    int bid;

public:
    Hand(const vector<string> &line)
    {
        bid = stoi(line[1]);
        for (int i = 0; i < line[0].size(); i++)
        {
            if (line[0][i] == 'T')
            {
                cards[i] = 10;
            }
            else if (line[0][i] == 'J')
            {
                cards[i] = 11;
            }
            else if (line[0][i] == 'Q')
            {
                cards[i] = 12;
            }
            else if (line[0][i] == 'K')
            {
                cards[i] = 13;
            }
            else if (line[0][i] == 'A')
            {
                cards[i] = 14;
            }
            else
            {
                cards[i] = line[0][i] - '0';
            }
        }
    }
    int *getCards() { return cards; }
    int getBid() { return bid; }

    bool resolveTie(const Hand &h)
    {
        for (int i = 0; i < 5; i++)
        {
            if (cards[i] != h.cards[i])
            {
                return (cards[i] < h.cards[i]);
            }
        }
        return false;
    }

    int determineType()
        const
    {
        map<int, int> occurences;
        for (int i = 0; i < 5; i++)
        {
            map<int, int>::iterator occIt = occurences.find(cards[i]);
            if (occIt == occurences.end())
            {
                occurences.insert(pair<int, int>(cards[i], 1));
            }
            else
            {
                occIt->second++;
            }
        }
        if (occurences.size() == 1)
        {
            return 6;
        }
        else if (occurences.size() == 2)
        {
            if (isNumberInMapValues(occurences, 4))
            {
                return 5;
            }
            else
            {
                return 4;
            }
        }
        else if (occurences.size() == 3)
        {
            if (isNumberInMapValues(occurences, 3))
            {
                return 3;
            }
            else
            {
                return 2;
            }
        }
        else if (occurences.size() == 4)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

    bool operator<(const Hand &h)
    {
        int type = determineType();
        int htype = h.determineType();
        if (type != htype)
        {
            return type < htype;
        }
        else
        {
            return resolveTie(h);
        }
    }
};

void problem()
{
    vector<string> ar = readInput();
    vector<Hand> hands;
    for (string a : ar)
    {
        hands.push_back(Hand(stringSplit(a, ' ')));
    }
    sort(hands.begin(), hands.end());
    int total = 0;
    for (int i = 0; i < hands.size(); i++)
    {
        total += (hands[i].getBid() * (i + 1));
        cout << "adding " << hands[i].getBid() << " * " << i + 1 << endl;
    }
    cout << total << endl;
}
