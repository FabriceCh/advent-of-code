#include <iostream>
#include <set>
#include <utility>
#include "cppUtils/stringTheory.cpp"
#include <numeric>
#include <chrono>

using namespace std;

enum Direction
{
    north,
    east,
    south,
    west,
    nope
};

Direction reverse(Direction d)
{
    return Direction((d + 2) % 4);
}

pair<int, int> getNextPosition(Direction d, int i, int j)
{
    if (d == north)
    {
        return pair<int, int>(i - 1, j);
    }
    else if (d == east)
    {
        return pair<int, int>(i, j + 1);
    }
    else if (d == south)
    {
        return pair<int, int>(i + 1, j);
    }
    else
    {
        return pair<int, int>(i, j - 1);
    }
}

class Node
{
private:
    char _symbol;

public:
    Node(char s) : _symbol(s){};
    pair<Direction, Direction> getConnectedDirections()
    {
        if (_symbol == '-')
        {
            return pair<Direction, Direction>(east, west);
        }
        else if (_symbol == '|')
        {
            return pair<Direction, Direction>(north, south);
        }
        else if (_symbol == 'L')
        {
            return pair<Direction, Direction>(north, east);
        }
        else if (_symbol == 'J')
        {
            return pair<Direction, Direction>(north, west);
        }
        else if (_symbol == '7')
        {
            return pair<Direction, Direction>(south, west);
        }
        else if (_symbol == 'F')
        {
            return pair<Direction, Direction>(south, east);
        }
        else
        {
            return pair<Direction, Direction>(nope, nope);
        }
    }
    Direction getNextDirection(Direction inD)
    {
        pair<Direction, Direction> connectedDs = getConnectedDirections();
        if (inD == connectedDs.first)
        {
            return connectedDs.second;
        }
    }
    bool isConnected(Direction d)
    {
        pair<Direction, Direction> connectedDs = getConnectedDirections();
        return (d == connectedDs.first || d == connectedDs.second);
    }
};

Direction findInitialPipes(int i, int j, vector<string> &ar)
{
    for (int d = 0; d < 4; d++)
    {
        Direction curd = Direction(d);
        pair<int, int> nextPos = getNextPosition(curd, i, j);
        Node node = Node(ar[nextPos.first][nextPos.second]);
        if (node.isConnected(reverse(curd)))
        {
            return curd;
        }
    }
}

pair<int, int> findSPos(vector<string> &ar)
{
    for (int i = 0; i < ar.size(); i++)
    {
        string l = ar[i];
        for (int j = 0; j < l.size(); j++)
        {
            char cc = l[j];
            if (cc == 'S')
            {
                return pair<int, int>(i, j);
            }
        }
    }
}

set<pair<int, int>> getLoop(vector<string> &ar, pair<int, int> &animalPos)
{
    set<pair<int, int>> loop;
    Direction currentLooks = findInitialPipes(animalPos.first, animalPos.second, ar);
    pair<int, int> currentPos = getNextPosition(currentLooks, animalPos.first, animalPos.second);
    currentLooks = reverse(currentLooks);
    int dis = 1;
    loop.insert(animalPos);
    loop.insert(currentPos);

    while (currentPos != animalPos)
    {
        Node node = Node(ar[currentPos.first][currentPos.second]);
        currentLooks = node.getNextDirection(currentLooks);
        currentPos = getNextPosition(currentLooks, currentPos.first, currentPos.second);
        currentLooks = reverse(currentLooks);
        dis++;
        loop.insert(currentPos);
    }
    return loop;
}

void printLoop(const vector<string> &ar, const set<pair<int, int>> &loop, const set<pair<int, int>> &insides)
{
    for (int i = 0; i < ar.size(); i++)
    {
        string l = ar[i];
        for (int j = 0; j < l.size(); j++)
        {
            if (loop.count(pair<int, int>(i, j)))
            {
                cout << "x";
            }
            else if (insides.count(pair<int, int>(i, j)))
            {
                cout << "I";
            }
            else
            {
                cout << ".";
            }
        }
        cout << endl;
    }
}

int nextNonLoopTileLineIndex(const string &line, int j, bool *inside)
{
    char sym = line[j];
    if (sym != 'L' && sym != 'F')
    {
        // cout << sym;
        *inside = !*inside;
        return j;
    }
    else
    {
        j++;
        cout << sym;
        while (line[j] == '-')
        {
            cout << '-';
            j++;
        }
        if ((sym == 'F' && line[j] == 'J') || (sym == 'L' && line[j] == '7'))
        {
            *inside = !*inside;
        }
        return j;
    }
}

void problem()
{
    vector<string> ar = readInput();
    pair<int, int> animalPos = findSPos(ar);

    set<pair<int, int>> loop = getLoop(ar, animalPos);
    set<pair<int, int>> insides;
    int total = 0;
    for (int i = 0; i < ar.size(); i++)
    {
        string l = ar[i];
        bool inside = false;
        for (int j = 0; j < l.size(); j++)
        {
            if (loop.count(pair<int, int>(i, j)))
            {
                j = nextNonLoopTileLineIndex(l, j, &inside);
                cout << ar[i][j];
            }
            else if (inside)
            {
                insides.insert(pair<int, int>(i, j));
                total++;
                cout << 'I';
            }
            else
            {
                cout << 'O';
            }
        }
        cout << endl;
    }
    // printLoop(ar, loop, insides);
    cout << "TOTAL: " << total << endl;
}
