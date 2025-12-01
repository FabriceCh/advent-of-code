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

Direction findInitialPipes(int i, int j, vector<string> ar)
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

void problem()
{
    pair<int, int> animalPos;
    vector<string> ar = readInput();
    for (int i = 0; i < ar.size(); i++)
    {
        string l = ar[i];
        for (int j = 0; j < l.size(); j++)
        {
            char cc = l[j];
            if (cc == 'S')
            {
                animalPos = pair<int, int>(i, j);
            }
        }
    }

    Direction currentLooks = findInitialPipes(animalPos.first, animalPos.second, ar);
    pair<int, int> currentPos = getNextPosition(currentLooks, animalPos.first, animalPos.second);
    currentLooks = reverse(currentLooks);
    int dis = 1;

    while (currentPos != animalPos)
    {
        cout << currentPos.first << " " << currentPos.second << endl;
        Node node = Node(ar[currentPos.first][currentPos.second]);
        currentLooks = node.getNextDirection(currentLooks);
        currentPos = getNextPosition(currentLooks, currentPos.first, currentPos.second);
        currentLooks = reverse(currentLooks);
        dis++;
    }
    cout << "total distance: " << dis << endl;
    cout << "dist/2: " << dis / 2 << endl;
}
