from queue import Queue
from Graph import GraphAL


def topological_sort(graph):
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = []

    q = []

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.append(i)

    while len(q) != 0:
        u = q.pop()

        sort_result.append(u)

        for adj_vertex in graph.get_adj_vertices(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.append(adj_vertex)

    if len(sort_result) != len(graph.adj_list):
        return None

    return sort_result

