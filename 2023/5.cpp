#include <iostream>
#include "cppUtils/stringTheory.cpp"
#include <limits>
#include "cppUtils/bigint.hpp"

using namespace std;

class MapSourceToDest
{
private:
    vector<BigInt> _sources;
    vector<BigInt> _dests;
    vector<BigInt> _ranges;

public:
    MapSourceToDest() : _sources({}), _dests({}), _ranges({})
    {
    }
    void addLine(string &line)
    {
        vector<string> parsedLine = stringSplit(line, ' ');
        _sources.push_back((parsedLine[1]));
        _dests.push_back((parsedLine[0]));
        _ranges.push_back((parsedLine[2]));
    }
    BigInt performMapping(BigInt input)
    {
        for (int i = 0; i < _sources.size(); i++)
        {
            if (input >= _sources[i] && input < _sources[i] + _ranges[i])
            {
                return _dests[i] + (input - _sources[i]);
            }
        }
        return input;
    }
};

void problem()
{
    vector<string> ar = readInput();
    vector<BigInt> seeds;
    vector<string> strSeeds = stringSplit(ar[0], ' ');
    for (int sid = 1; sid < strSeeds.size(); sid++)
    {
        seeds.push_back((strSeeds[sid]));
    }

    vector<MapSourceToDest> allMaps;

    MapSourceToDest currentMap = MapSourceToDest();
    bool isReadingMap = false;
    for (int i = 3; i < ar.size(); i++)
    {

        if (ar[i] == "")
        {
            i++;
            allMaps.push_back(currentMap);
            currentMap = MapSourceToDest();
            continue;
        }
        currentMap.addLine(ar[i]);
    }
    BigInt lowestNum;
    lowestNum = "999999999999999999999999999999999999999999999";
    for (BigInt currentSeed : seeds)
    {

        for (MapSourceToDest currentMap : allMaps)
        {
            currentSeed = currentMap.performMapping(currentSeed);
        }
        if (currentSeed < lowestNum)
        {
            lowestNum = currentSeed;
        }
    }
    cout << lowestNum << endl;
}