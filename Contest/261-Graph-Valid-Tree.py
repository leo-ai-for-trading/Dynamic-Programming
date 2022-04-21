# Problem is free on Lintcode 
"""
- tree is not allowed to have a loop
- a tree needs to be connected
- dfs
- if number of visited matches it means they are connected
- must be not cycle
- add the previous value to the node to avoid cycle
- the previous value fit into 0 is -1 because no nodes are gonna have this value as they start with 0
- 
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if not n:
            return True         
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True 
        
        return dfs(0, -1) and n == len(visit)
