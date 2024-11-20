from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        values_seen = set()
        values_seen.add(edges[0][0])
        values_seen.add(edges[0][1])
        if edges[1][0] in values_seen:
            return edges[1][0]
        else:
            return edges[1][1]


if __name__ == '__main__':
    test_cases = ( ([[1,2],[2,3],[4,2]], 2), ([[1,2],[5,1],[1,3],[1,4]], 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().findCenter(case[0])) + '\n')