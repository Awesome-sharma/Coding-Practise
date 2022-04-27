# 1791. Find Center of Star Graph

# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi.
# Return the center of the given star graph.


# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

  
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

# CODE --

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hash_map = {}
        for i in edges:
            if i[0] not in hash_map:
                val = i[0]
                hash_map[val]=1
            else:
                hash_map[i[0]] += 1
            if i[1] not in hash_map:
                val = i[1]
                hash_map[val] = 1
            else:
                hash_map[i[1]] += 1

        for j in hash_map:
            if hash_map[j] == len(edges):
              return j
              break
        
        
