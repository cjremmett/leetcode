from typing import List
from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counts = defaultdict(int)
        for edge in roads:
            counts[edge[0]] += 1
            counts[edge[1]] += 1

        counts_ord = sorted(list(counts.values()))
        
        sum = 0
        for i in reversed(range(n - len(counts_ord) + 1, n + 1)):
            sum += i * counts_ord[-1 * (n - i + 1)]
            
        return sum

if __name__ == '__main__':
    test_cases = ( (5, [[0,1]], 9), (5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]], 43), (5, [[0,3],[2,4],[1,3]], 20))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().maximumImportance(case[0], case[1])) + '\n')