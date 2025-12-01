#include "cppUtils/dijkstra.cpp"

int problem()
{
    Node start = Node(1);
    Node node2 = Node(2);
    Node node3 = Node(3);
    Node node4 = Node(4);
    Node node5 = Node(5);
    Node node6 = Node(6);
    Node node7 = Node(7);
    Node node8 = Node(8);
    Node node9 = Node(9);
    start.addNeighbor(node2);
    start.addNeighbor(node3);
    node2.addNeighbor(node4);
    node3.addNeighbor(node4);
    node3.addNeighbor(node7);
    node3.addNeighbor(node5);
    node4.addNeighbor(node8);
    node5.addNeighbor(node6);
    node6.addNeighbor(node9);
    node7.addNeighbor(node9);
    node8.addNeighbor(node7);

    dijkstra(&start, 9);
    return 0;
}