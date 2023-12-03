#include <vector>

class Node
{
private:
    std::vector<Node *> _neighbors;
    int _value;

public:
    Node(int value);
    void addNeighbor(Node &node);
    int getValue();
    std::vector<Node *> getNeighbors();
};