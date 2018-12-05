# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 6 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 12/3/2018
# PURPOSE: To use and manipulate a Graph data structure.
# **********************************************************************************************************************

import Graph
import DisjointSetForest


def kruskals_algorithm(graph):
    """
    Kruskals Algorithm based off professors implementation.
    Sorts edges by increasing cost.
    :param graph:
    :return:
    """
    sorted_list = get_edges_by_increase_cost(graph)
    # print(sorted_list)
    path = []

    min_tree = DisjointSetForest.DisjointSetForest(len(sorted_list))
    # for value in sorted_list:
    #     print(value[0], value[1], value[2])
    for i in range(len(min_tree.dsf)):
        # print('Inserting: ', sorted_list[i][1], sorted_list[i][2])
        if min_tree.find(sorted_list[i][2]) != min_tree.find(sorted_list[i][1]):
            min_tree.union(sorted_list[i][1], sorted_list[i][2])
            path.append(sorted_list[i])
        # print(path)

    return path


def get_edges_by_increase_cost(graph):
    """
    Used in Kruskols Algorithm. Returns a list of the weights in ascending order of a graph.
    :param graph:
    :return sorted_list:
    """

    weights_list = []
    check = []
    seen = False

    for i in range(len(graph.adj_list)):
        temp = graph.adj_list[i]
        while temp is not None:
            for j in range(len(check)):
                if (check[j][0] == i or check[j][0] == temp.item) and (check[j][1] == i or check[j][1] == temp.item):
                    seen = True

            if seen == False:
                weights_list.append([temp.weight, i, temp.item])
                check.append([i, temp.item])
            seen = False
            temp = temp.next

    sorted_list = sorted(weights_list)

    return sorted_list



