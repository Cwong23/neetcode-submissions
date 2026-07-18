class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # trying to find redundant edge
        # return last edge in edges if there are multiple redundant edges

        # remove edges where the number only shows up once
        # 1,2 1,3 3,4 2,4 <-
        
        # 1,2 1,3 1,4 3,4 4,5
        # 1,3 1,4 3,4 <-

        # loop over all edges
        # store the edges that only appear once
            # dict value : index
            # if the edge exists in dict, then add to set
            # remove all the edges from the dict that exist in set
        # delete those edges
        # keep order b/c we need to return last if multiple redunandcies
        # if set is empty, return last edge

        while True:
            l = len(edges)
            dup = set()
            occur_edges = {}
            for i, edge in enumerate(edges):
                for val in edge:
                    if val in occur_edges:
                        dup.add(val)
                    else:
                        occur_edges[val] = i
            
            for d in dup:
                del occur_edges[d]
            
            for i in range(len(edges) - 1, -1 , -1):
                edge = edges[i]
                for val in edge:
                    if val in occur_edges:
                        del edges[i]
            if len(edges) == l:
                break
        
        return edges[-1]
