#include <iostream>
#include "cppUtils/stringTheory.cpp"
#include <limits>
#include "cppUtils/bigint.hpp"
#include <utility>
#include <algorithm>

using namespace std;

class Interval
{
private:
    BigInt _lowerBound;
    BigInt _upperBound;

public:
    Interval(BigInt lowerBound, BigInt upperBound) : _lowerBound(lowerBound), _upperBound(upperBound) {}
    Interval(Interval *interval) : _lowerBound(interval->_lowerBound), _upperBound(interval->_upperBound) {}

    BigInt getLowerBound()
    {
        return _lowerBound;
    }

    bool isIntersecting(Interval *sourceInterval)
    {
        return (!(sourceInterval->_lowerBound > _upperBound || sourceInterval->_upperBound < _lowerBound));
    }

    vector<Interval> reunion(Interval &other)
    {
        if (other._lowerBound > _upperBound || other._upperBound < _lowerBound)
        {
            return {Interval(this), other};
        }
        return {Interval(min(_lowerBound, other._lowerBound), max(_upperBound, other._upperBound))};
    }

    vector<Interval> difference(Interval *sourceInterval)
    {
        vector<Interval> extensions;
        // extension in upper bound
        if (sourceInterval->_upperBound < _upperBound)
        {
            extensions.push_back(Interval(sourceInterval->_upperBound, _upperBound));
        }
        // extension in lower bound
        if (sourceInterval->_lowerBound > _lowerBound)
        {
            extensions.push_back(Interval(_lowerBound, sourceInterval->_lowerBound));
        }
        return extensions;
    }

    Interval intersect(Interval *sourceInterval)
    {
        // source's start is in
        if (_lowerBound <= sourceInterval->_lowerBound && sourceInterval->_lowerBound <= _upperBound)
        {
            BigInt resultingUpperBound = _upperBound;
            if (sourceInterval->_upperBound < _upperBound)
            {
                resultingUpperBound = sourceInterval->_upperBound;
            }
            return Interval(sourceInterval->_lowerBound, resultingUpperBound);
        }
        // source's end is in
        else if (_lowerBound <= sourceInterval->_upperBound && sourceInterval->_upperBound <= _upperBound)
        {
            BigInt resultingLowerBound = _lowerBound;
            if (sourceInterval->_lowerBound > _lowerBound)
            {
                resultingLowerBound = sourceInterval->_lowerBound;
            }
            return Interval(resultingLowerBound, sourceInterval->_upperBound);
        }
        // this is included in source
        else if ((sourceInterval->_lowerBound <= _lowerBound && _lowerBound <= sourceInterval->_upperBound))
        {
            return Interval(this);
        }
        else
        {
            cout << "don't call intersect() if the intervals don't intersect you silly goose!" << endl;
            return Interval(0, 0);
        }
    }
    friend Interval operator+(Interval i, BigInt &offset)
    {
        i._lowerBound += offset;
        i._upperBound += offset;
        return i;
    }
};

class MapIntervalsSourceToDest
{
private:
    vector<Interval> _sources;
    vector<BigInt> _offsets;

public:
    MapIntervalsSourceToDest() : _sources({}), _offsets({}) {}
    void addLine(string line)
    {
        vector<string> parsedLine = stringSplit(line, ' ');
        BigInt source, dest, range;
        dest = parsedLine[0];
        source = parsedLine[1];
        range = parsedLine[2];
        Interval sourceInterval = Interval(source, source + range - 1);
        _sources.push_back(sourceInterval);
        _offsets.push_back(dest - source);
    }
    vector<Interval> performMapping(Interval &hihi)
    {
        vector<Interval> results;
        vector<Interval> extensionsIntervals = {hihi};
        for (int i = 0; i < _sources.size(); i++)
        {
            vector<Interval> new_extensions;
            for (Interval hehe : extensionsIntervals)
            {

                if (hehe.isIntersecting(&_sources[i]))
                {
                    Interval resultingInterval = hehe.intersect(&_sources[i]) + _offsets[i];
                    results.push_back(resultingInterval);
                    vector<Interval> diff = hehe.difference(&_sources[i]);
                    new_extensions.insert(extensionsIntervals.end(), diff.begin(), diff.end());
                }
                else
                {
                    new_extensions.push_back(hehe);
                }
            }
            extensionsIntervals = new_extensions;
        }
        results.insert(results.end(), extensionsIntervals.begin(), extensionsIntervals.end());
        return results;
    }
    vector<Interval> performMappingPass(vector<Interval> &intervals)
    {
        vector<Interval> newIntervals;
        for (Interval inter : intervals)
        {
            vector<Interval> mappedIntervals = performMapping(inter);
            newIntervals.insert(newIntervals.end(), mappedIntervals.begin(), mappedIntervals.end());
        }
        return newIntervals;
    }
};

vector<Interval> retrieveIntervalsFromFirstLine(string &line)
{
    vector<Interval> intervals;
    vector<string> strSeeds = stringSplit(line, ' ');
    for (int i = 1; i < strSeeds.size(); i += 2)
    {
        BigInt start, end, range;
        start = strSeeds[i];
        range = strSeeds[i + 1];
        end = start + range - 1;
        intervals.push_back(Interval(start, end));
    }
    return intervals;
}

BigInt getSmallestLowerBounds(vector<Interval> &intervals)
{
    BigInt lowestNum;
    lowestNum = "999999999999999999999999999999999999999999999";
    for (Interval inter : intervals)
    {
        if (inter.getLowerBound() < lowestNum)
        {
            lowestNum = inter.getLowerBound();
        }
    }
    return lowestNum;
}

void problem()
{

    vector<string> ar = readInput("testinput");
    cout << "Loading the seeds" << endl;
    vector<Interval> theIntervals = retrieveIntervalsFromFirstLine(ar[0]);

    vector<MapIntervalsSourceToDest> allMaps;

    MapIntervalsSourceToDest currentMap = MapIntervalsSourceToDest();
    bool isReadingMap = false;
    for (int i = 3; i < ar.size(); i++)
    {

        if (ar[i] == "")
        {
            i++;
            allMaps.push_back(currentMap);
            currentMap = MapIntervalsSourceToDest();
            continue;
        }
        currentMap.addLine(ar[i]);
    }

    for (MapIntervalsSourceToDest map : allMaps)
    {
        theIntervals = map.performMappingPass(theIntervals);
    }
    cout << getSmallestLowerBounds(theIntervals) << endl;
}

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

void problem1()
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