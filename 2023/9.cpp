#include <iostream>
#include <utility>
#include "cppUtils/stringTheory.cpp"
#include <numeric>
#include <chrono>

using namespace std;

int find_next(vector<int> nums)
{
    vector<int> nextSequence;
    bool isAllZeros = true;
    for (int i = 0; i < nums.size() - 1; i++)
    {
        int diff = nums[i + 1] - nums[i];
        nextSequence.push_back(diff);
        isAllZeros = (isAllZeros && diff == 0);
    }

    if (isAllZeros)
    {
        return nums[nums.size() - 1];
    }
    else
    {
        int below = find_next(nextSequence);
        return below + nums[nums.size() - 1];
    }
}

int find_previous(vector<int> nums)
{
    vector<int> nextSequence;
    bool isAllZeros = true;
    for (int i = 0; i < nums.size() - 1; i++)
    {
        int diff = nums[i + 1] - nums[i];
        nextSequence.push_back(diff);
        isAllZeros = (isAllZeros && diff == 0);
    }

    if (isAllZeros)
    {
        return nums[0];
    }
    else
    {
        int below = find_previous(nextSequence);
        return nums[0] - below;
    }
}

void problem()
{
    vector<string> ar = readInput();
    long total = 0;

    for (string l : ar)
    {
        vector<int> nums;
        vector<string> strNums = stringSplit(l, ' ');
        for (string strn : strNums)
        {
            nums.push_back(stoi(strn));
        }
        int ans = find_previous(nums);
        total += ans;
    }
    cout << "total: " << total << endl;
}