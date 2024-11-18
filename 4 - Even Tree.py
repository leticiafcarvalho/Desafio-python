#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    
    graph = {i: [] for i in range(1, t_nodes + 1)}
    for u, v in zip(t_from, t_to):
        graph[u].append(v)
        graph[v].append(u)
        
    subtree_count = [0] * (t_nodes + 1)
    removable_edges = 0  

    def dfs(node, parent):
        nonlocal removable_edges
        subtree_count[node] = 1  
        for neighbor in graph[node]:
            if neighbor != parent:
                subtree_count[node] += dfs(neighbor, node)
        if subtree_count[node] % 2 == 0 and parent is not None:
            removable_edges += 1
        return subtree_count[node]

    dfs(1, None)
    
    return removable_edges

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
