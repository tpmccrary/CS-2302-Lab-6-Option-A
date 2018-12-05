# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 6 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 12/3/2018
# PURPOSE: To use and manipulate a Graph data structure.
# **********************************************************************************************************************

class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        return self.find(self.dsf[a])

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        self.dsf[rb] = ra

    def get_num_sets(self):
        count = 0

        for num in self.dsf:
            if num < 0:
                count += 1

        return count

    def is_leaf(self, k):
        count = 0

        for num in self.dsf:
            if num == k:
                return False

        return True

    def get_largest_set(self, k):
        max_size = 0



        return max_size


def create_dsf(n, k):
    dsf = [-1] * (n * k)

    for i in range(len(dsf)):
        if i % k != 0:
            dsf[i] = i - 1

    return dsf