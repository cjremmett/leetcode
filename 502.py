from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mapping = [(capital[i], profits[i]) for i in range(0, len(capital))]
        mapping.sort(key = lambda x: x[0])

        projects_heap = []
        i = 0
        for _ in range(0, k):
            while i < len(mapping) and mapping[i][0] <= w:
                heapq.heappush(projects_heap, -mapping[i][1])
                i += 1
            if len(projects_heap) == 0:
                break
            else:
                w -= heapq.heappop(projects_heap)

        return w


if __name__ == '__main__':
    test_cases = ( (2, 0, [1,2,3], [0,1,1], 4), (3, 0, [1,2,3], [0,1,2], 6))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + ', ' + str(case[3]) + '\nExpected output: ' + str(case[4]) + '\nActual output: ' + str(Solution().findMaximizedCapital(case[0], case[1], case[2], case[3])) + '\n')