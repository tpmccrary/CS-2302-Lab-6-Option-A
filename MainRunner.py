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
import time


def main():
    """
    Main function/Runner function.
    :return:
    """
    # ======================
    # TOPOLOGICAL SORT TESTS
    # ======================
    print('======================\nTOPOLOGICAL SORT TESTS\n======================')

    # __________TEST 1__________
    print('__________Test 1 - Directed, Acyclic, Graph__________')
    start_time = time.time()
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

    top_sort = TopologicalSort.topological_sort(graph)
    print("Running time = %s seconds" % (time.time() - start_time))
    print_top_sort(top_sort)

    # __________TEST 2__________
    print('\n__________Test 2 - Another Directed, Acyclic, Graph__________')
    start_time = time.time()
    graph = Graph.GraphAL(6, True)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    graph.add_edge(4, 5)
    graph.add_edge(5, 2)

    top_sort = TopologicalSort.topological_sort(graph)
    print("Running time = %s seconds" % (time.time() - start_time))
    print_top_sort(top_sort)

    # __________TEST 3__________
    print('\n__________Test 3 - No Vertices__________')
    start_time = time.time()
    graph = Graph.GraphAL(0, True)

    top_sort = TopologicalSort.topological_sort(graph)
    print("Running time = %s seconds" % (time.time() - start_time))
    print_top_sort(top_sort)

    # ========================
    # KRUSKALS ALGORITHM TESTS
    # ========================
    print('\n\n=========================\nKRUSKALS ALGORITHMS TESTS\n=========================')

    # __________TEST 1__________
    print('__________Test 1 - Non Directed Graph__________')
    start_time = time.time()
    graph = Graph.GraphAL(8, False)  # Creates graph.

    # Adds edges between vertices.
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

    kru_alg = KruskalsAlgorithm.kruskals_algorithm(graph)
    print("Running time = %s seconds" % (time.time() - start_time))
    print_kru_alg(kru_alg)

    # __________TEST 2__________
    print('\n__________Test 2 - Another Non Directed Graph__________')
    start_time = time.time()
    graph = Graph.GraphAL(4, False)  # Creates graph.

    # Adds edges between vertices.
    graph.add_edge(0, 1, 1)
    graph.add_edge(0, 2, 2)
    graph.add_edge(0, 3, 3)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 4)
    graph.add_edge(2, 3, 5)

    kru_alg = KruskalsAlgorithm.kruskals_algorithm(graph)
    print("Running time = %s seconds" % (time.time() - start_time))
    print_kru_alg(kru_alg)

    # __________TEST 3__________
    print('\n__________Test 3 - No Vertices__________')
    start_time = time.time()
    graph = Graph.GraphAL(0, False)  # Creates graph.

    kru_alg = KruskalsAlgorithm.kruskals_algorithm(graph)
    print("Running time = %s seconds" % (time.time() - start_time))
    print_kru_alg(kru_alg)


def print_top_sort(top_sort):
    """
    Prints Topological sort of graph.
    :param top_sort:
    :return:
    """
    if top_sort is None:
        return

    print('Topological sort for this graph(as vertices): ', end='')

    for value in top_sort:
        print('(', value, ')-->', end='')


def print_kru_alg(kru_alg):
    """
    Prints the min spanning tree of graph obtained from Kruskals Algorithm.
    :param kru_alg:
    :return:
    """
    if kru_alg is None:
        return

    print('Kruskals Algorithm Minimum Spanning Tree for this graph: ', end='')

    for value in kru_alg:
        print('(', value[1], ')--(', value[2], '), ', end='')


if __name__ == '__main__':
    main()