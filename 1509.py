from typing import List
from bisect import insort_left

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        nums.sort()
        min_dif = nums[-1] - nums[0]
        for i in range(0, 4):
            min_dif = min(min_dif, nums[i - 4] - nums[i])

        return min_dif
        
    
if __name__ == '__main__':
    test_cases = ( ([6,6,0,1,1,4,6], 2), ([5,3,2,4], 0), ([1,5,0,10,14], 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual ouput: ' + str(Solution().minDifference(case[0])) + '\n')