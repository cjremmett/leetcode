from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if len(heap) < k or nums1[i] + nums2[j] <= (heap[0][0] + heap[0][1]):
                    heapq.heappush(heap, [nums1[i], nums2[j]])
                    heap = heapq.nlargest(k, heap, key= lambda x: -1 * (x[0] + x[1]))
        
        return heap
    
if __name__ == '__main__':
    test_cases = ( ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]), ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + ', ' + str(case[2]) + '\nExpected output: ' + str(case[3]) + '\nActual output: ' + str(Solution().kSmallestPairs(case[0], case[1], case[2])) + '\n')