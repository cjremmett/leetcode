from typing import List
from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        node_edges = defaultdict(set)
        for edge in edges:
            node_edges[edge[1]].add(edge[0])

        ret_list = []
        for i in range(0, n):
            ancestors = set()
            self.get_ancestors(node_edges, i, ancestors)
            ret_list.append(sorted(list(ancestors)))

        return ret_list
        
    def get_ancestors(self, edges_dict, node, prev_edges):
        for ancestor in edges_dict[node]:
            if ancestor not in prev_edges:
                prev_edges.add(ancestor)
                self.get_ancestors(edges_dict, ancestor, prev_edges)


if __name__ == '__main__':
    test_cases = ( (8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]], [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]), (5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]], [[],[0],[0,1],[0,1,2],[0,1,2,3]]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().getAncestors(case[0], case[1])) + '\n')