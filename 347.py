class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return []

if __name__ == '__main__':
    test_cases = ( ([1,1,1,2,2,3], 2, [1,2]), ([1], 1, [1]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', k=' + str(case[1]) + '\nExpeted output: ' + str(case[2]) + '\nActual output: ' + str(Solution().topKFrequent(case[0], case[1])) + '\n')