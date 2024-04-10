from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return []
    
if __name__ == '__main__':
    test_cases = ( ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]), ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().kSmallestPairs(case[0], case[1], case[2])) + '\n')