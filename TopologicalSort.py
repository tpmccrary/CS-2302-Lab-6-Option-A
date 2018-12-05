# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 6 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 12/3/2018
# PURPOSE: To use and manipulate a Graph data structure.
# **********************************************************************************************************************

from queue import Queue
from Graph import GraphAL


def topological_sort(graph):
    """
    Topological Sort, based off professors implementation.
    MUST BE A DIRECTED AND ACYCLIC GRAPH(no cycles)!
    Returns a list of vertices that make a path from one X to vertex Y, with X always before Y in the list.
    :param graph:
    :return Sort Result:
    """
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = []

    q = []

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.append(i)

    while len(q) != 0:
        u = q.pop()

        sort_result.append(u)

        for adj_vertex in graph.get_adj_vertices_list(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.append(adj_vertex)

    if len(sort_result) != len(graph.adj_list):
        return None

    return sort_result


def compute_indegree_every_vertex(graph):
    """
    Computes the indegree for every vertix and returns a list, with the index of the list representing the vertex, and
    the number within representing the amount of indegrees.
    :param graph:
    :return indegree_list:
    """
    if graph is None:
        return

    indegree_list = [0] * len(graph.adj_list)

    for i in range(len(graph.adj_list)):
        temp = graph.adj_list[i]
        while temp is not None:
            indegree_list[temp.item] = indegree_list[temp.item] + 1
            temp = temp.next

    return indegree_list