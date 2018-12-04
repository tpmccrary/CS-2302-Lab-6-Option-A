import DisjointSetForest
import Graph
import TopologicalSort


def main():
    graph = Graph.GraphAL(3, True)
    graph.add_edge(0, 1)
    # graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)

    print(graph.adj_list)
    for i in range(len(graph.adj_list)):
        temp = graph.adj_list[i]
        while temp is not None:
            print('Index:', i, '\tItem =', temp.item)
            temp = temp.next

    # print(TopologicalSort.topological_sort(graph))

    print(graph.get_vertex_in_degree(2))
    print(graph.get_vertex_in_degree(0))

    print(graph.is_there_a_two_vertex_cycle())








if __name__ == '__main__':
    main()