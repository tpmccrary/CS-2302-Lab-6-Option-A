class GraphALNode:
    def __init__(self, item, weight, next):
        self.item = item
        self.weight = weight
        self.next = next


class GraphAL:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        #  TODO: What if src already points to dest?
        self.adj_list[src] = GraphALNode(dest, weight, self.adj_list[src])

        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, weight, self.adj_list[dest])

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        if self.adj_list[src] is None:
            return

        if self.adj_list[src].item == dest:
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

        return len(self.adj_list)

    def get_num_vertices(self):
        return len(self.adj_list)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    def get_vertex_in_degree(self, vertex):
        """
        Solution to Problem 6: Returns in degree of a vertex.
        :param vertex:
        :return in_degree_count:
        """

        if not self.is_valid_vertex(vertex):
            return

        in_degree_count = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]
            while temp is not None:
                if temp.item == vertex:
                    in_degree_count = in_degree_count + 1
                temp = temp.next

        return in_degree_count

    def is_there_a_two_vertex_cycle(self):
        """
        Solution to Problem 7: Returns True if cycle of size 2 is found.
        :return True, False:
        """
        count = 0
        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]
            while temp is not None:
                count = temp.item
                temp2 = self.adj_list[count]
                while temp2 is not None:
                    if temp2.item == i:
                        return True
                    temp2 = temp2.next
                temp = temp.next
        return False


    def


    def get_adj_vertices(self, vertex):
        """
        Returns list of adjacent vertices from one vertex
        """

        adj = list()

        temp = self.adj_list[vertex]

        while temp != None:
            adj.append(temp.item)

            temp = temp.next

        return adj