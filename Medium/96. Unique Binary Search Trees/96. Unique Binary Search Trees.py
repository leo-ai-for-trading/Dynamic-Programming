class Solution:
    def numTrees(self, n: int) -> int:
        '''
        Reasoning
        -  recursive problem
        - at some point one value coul become the root
        - to get the number of combinations we re gonna multiply the numTrees
        - dp problem: solve sub problems
        - O(n^2)
        '''
        #to get numsTrees[4] = numTrees[0] * numTrees[3] +
        #                      numTree[1]*numTree[2]  +
        #this one is the left subtrees
        numtree = [1]*(n+1)
        # 0 nodes = 1 tree, the empty one
        #1 nodes = 1 tree
        for nodes in range(2,n+1):
            tot = 0
            for root in range(1,nodes + 1):
                left = root -1 #left sub tree
                right = nodes - root
                tot += numtree[left] * numtree[right]
            numtree[nodes] = tot
        return numtree[n]
