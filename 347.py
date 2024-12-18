from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = defaultdict(int)
        for i in range(0, len(nums)):
            map[nums[i]] += 1

        return heapq.nlargest(k, map.keys(), key=lambda x: map[x])

if __name__ == '__main__':
    test_cases = ( ([1,1,1,2,2,3], 2, [1,2]), ([1], 1, [1]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', k=' + str(case[1]) + '\nExpeted output: ' + str(case[2]) + '\nActual output: ' + str(Solution().topKFrequent(case[0], case[1])) + '\n')