#include "cppUtils/stringTheory.cpp"
#include <map>
#include <utility>

using namespace std;

const int GRID_SIZE = 140;

bool isDigit(char c)
{
    return (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9');
}

vector<vector<int>> getNeighbors(int x, int y)
{
    return {
        {x - 1, y - 1}, {x - 1, y}, {x - 1, y + 1}, {x, y - 1}, {x, y + 1}, {x + 1, y - 1}, {x + 1, y}, {x + 1, y + 1}};
}

bool isNeighborSymbol(int i, int j, vector<string> &ar)
{
    if (i >= 0 && i < GRID_SIZE && j >= 0 && j < GRID_SIZE)
    {
        if (!isDigit(ar[i][j]) && ar[i][j] != '.')
        {
            return true;
        }
    }
    return false;
}

bool isNeighborGear(int i, int j, vector<string> &ar)
{
    if (i >= 0 && i < GRID_SIZE && j >= 0 && j < GRID_SIZE)
    {
        if (ar[i][j] == '*')
        {
            return true;
        }
    }
    return false;
}

void updateGearsMap(std::map<std::pair<int, int>, std::vector<int>> &gears, int i, int j, int number)
{
    std::pair<int, int> gearPosition(i, j);
    std::vector<int> numbers = {number};
    std::map<std::pair<int, int>, std::vector<int>>::iterator gearNumbersIt = gears.find(gearPosition);
    if (gearNumbersIt == gears.end())
    {
        gears.insert(std::pair<std::pair<int, int>, std::vector<int>>(gearPosition, numbers));
    }
    else
    {
        gearNumbersIt->second.push_back(number);
    }
}

int problem2()
{
    vector<string> ar = readInput();
    map<pair<int, int>, vector<int>> gearsMap;
    for (int i = 0; i < ar.size(); i++)
    {
        string current_number = "";
        bool current_gear = false;
        int gear_i, gear_j;
        for (int j = 0; j < GRID_SIZE; j++)
        {
            if (isDigit(ar[i][j]))
            {
                vector<vector<int>> neighs = getNeighbors(i, j);
                for (vector<int> neigh : neighs)
                {
                    if (isNeighborGear(neigh[0], neigh[1], ar))
                    {
                        gear_i = neigh[0];
                        gear_j = neigh[1];
                        current_gear = true;
                    }
                }
                current_number += ar[i][j];
                if (j == GRID_SIZE - 1 && current_gear)
                {
                    cout << current_number << endl;
                    updateGearsMap(gearsMap, gear_i, gear_j, stoi(current_number));
                }
            }
            else
            {

                if (current_number.size() > 0)
                {
                    if (current_gear)
                    {
                        cout << current_number << endl;
                        updateGearsMap(gearsMap, gear_i, gear_j, stoi(current_number));
                    }
                    current_number = "";
                    current_gear = false;
                }
            }
        }
    }
    int total = 0;
    for (auto const &gearEntry : gearsMap)
    {
        cout << "gearposition: " << gearEntry.first.first << ',' << gearEntry.first.second << " numbers: ";
        for (int const num : gearEntry.second)
        {
            cout << num << ",";
        }
        cout << endl;
        if (gearEntry.second.size() == 2)
        {
            total += (gearEntry.second[0] * gearEntry.second[1]);
        }
    }

    cout << "total:" << total << endl;
    return 0;
}

int problem1()
{
    vector<string> ar = readInput();
    int total = 0;
    for (int i = 0; i < ar.size(); i++)
    {
        string current_number = "";
        bool current_symbol = false;
        for (int j = 0; j < GRID_SIZE; j++)
        {
            if (isDigit(ar[i][j]))
            {
                vector<vector<int>> neighs = getNeighbors(i, j);
                for (vector<int> neigh : neighs)
                {
                    current_symbol = isNeighborSymbol(neigh[0], neigh[1], ar) || current_symbol;
                }
                current_number += ar[i][j];
                if (j == GRID_SIZE - 1 && current_symbol)
                {
                    cout << current_number << endl;
                    total += stoi(current_number);
                }
            }
            else
            {

                if (current_number.size() > 0)
                {
                    if (current_symbol)
                    {
                        cout << current_number << endl;
                        total += stoi(current_number);
                    }
                    current_number = "";
                    current_symbol = false;
                }
            }
        }
    }
    cout << "total:" << total << endl;
    return 0;
}
