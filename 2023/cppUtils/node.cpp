#include "node.h"
#include <vector>

Node::Node(int value) : _neighbors({}), _value(value) {}

int Node::getValue() { return this->_value; }

std::vector<Node *> Node::getNeighbors() { return this->_neighbors; }

void Node::addNeighbor(Node &node)
{
    this->_neighbors.push_back(&node);
}
