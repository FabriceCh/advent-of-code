#include "node.cpp"
#include <iostream>
#include <map>

std::vector<Node *> dijkstra(Node *startingNode, int endingNodeValue)
{
    std::map<Node *, int> distances = {
        {startingNode, 0}};
    std::vector<Node *> answer;
    Node myNode = Node(6);
    std::cout << myNode.getValue() << std::endl;

    return answer;
}
