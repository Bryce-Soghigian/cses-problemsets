# -*- coding: utf-8 -*-
"""
You are given a tree consisting of n nodes.

Your task is to determine for each node the maximum distance to another node.

Input

The first input line contains an integer n: the number of nodes. The nodes are numbered 1,2,…,n.

Then there are n−1 lines describing the edges. Each line contains two integers a and b: there is an edge between nodes a and b.

Output

Print n integers: for each node 1,2,…,n, the maximum distance to another node.

Constraints
1≤n≤2⋅105
1≤a,b≤n
Example

Input:
5
1 2
1 3
3 4
3 5

             1
            / \
           2   3
               /\
              4  5

Output:
2 3 2 3 3

"""
from collections import defaultdict, deque
class TestSolution:
    def test_main():
        pass
class Solution:
    def _build_graph(self, n, edges):
        graph = defaultdict([])

        for i in range(1, n):
            graph[i] = []
        
        for src,dest in edges.items():
            graph[src].append(dest)
            graph[dest].append(src)

        return graph

    def bfs(tree,i):

        queue = deque([(i,1)])
        seen = set()
        maximum_level = 0
        while queue:
            curr, level = queue.popleft()
            seen.add(curr)
            maximum_level = max(level, maximum_level)
            for child in tree[curr]:
                if child not in seen:
                    queue.append((child, level + 1))
        
        return maximum_level

    def __call__(self, n, edges):
        """
        Approaches

        1. Brute Force
        For Each Node in the tree we can dfs and find teh farthest node away from it

        2. MST


        3. Topological Sort
        """
        tree = self._build_graph(n, edges)
        for i in range(1, n):
            yield self._dfs(tree,i)
    
    


if __name__ == "__main__":
    main = Solution()
    n = int(input())
    edges = map(int, input().split())
    print(main(n,edges))