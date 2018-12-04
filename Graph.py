# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 6 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 12/3/2018
# PURPOSE: To use and manipulate a Graph data structure.
# **********************************************************************************************************************

import DisjointSetForest
import Graph
import TopologicalSort
import KruskalsAlgorithm


def main():
    """
    Main function/Runner function.
    :return:
    """
    # ======================
    # TOPOLOGICAL SORT TESTS
    # ======================
    print('__________Test 1 - Acyclic graph__________')
    graph = Graph.GraphAL(9, True)

    graph.add_edge(0, 1)
    graph.add_edge(2, 1)
    graph.add_edge(3, 2)
    graph.add_edge(3, 6)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(5, 1)
    graph.add_edge(5, 2)
    graph.add_edge(5, 4)
    graph.add_edge(5, 7)
    graph.add_edge(6, 2)
    graph.add_edge(6, 5)
    graph.add_edge(6, 8)
    graph.add_edge(7, 4)
    graph.add_edge(8, 5)
    graph.add_edge(8, 7)

    print('Topological sort for this graph:', TopologicalSort.topological_sort(graph))

    # ========================
    # KRUSKALS ALGORITHM TESTS
    #=========================

    print('Test 1 - Kruskals Algorithm')

    graph = Graph.GraphAL(8, False)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 4, 3)
    graph.add_edge(1, 2, 9)
    graph.add_edge(1, 4, 6)
    graph.add_edge(1, 5, 8)
    graph.add_edge(2, 3, 10)
    graph.add_edge(2, 5, 7)
    graph.add_edge(2, 6, 15)
    graph.add_edge(3, 6, 16)
    graph.add_edge(4, 5, 1)
    graph.add_edge(4, 7, 4)
    graph.add_edge(5, 6, 12)
    graph.add_edge(5, 7, 11)
    graph.add_edge(6, 7, 13)

    for i in range(len(graph.adj_list)):
        temp = graph.adj_list[i]
        print('Vertex:', i)
        while temp is not None:
            print(temp.item)
            temp = temp.next

    print('Kruskals Algorithm for this graph:', KruskalsAlgorithm.kruskals_algorithm(graph))





if __name__ == '__main__':
    main()
