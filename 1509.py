from typing import List
from bisect import insort_left

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        nums.sort()
        for i in range(0, 3):
            if nums[1] - nums[0] > nums[-1] - nums[-2]:
                nums.pop(0)
            else:
                nums.pop()

        return nums[-1] - nums[0]
        
    
if __name__ == '__main__':
    test_cases = ( ([5,3,2,4], 0), ([1,5,0,10,14], 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual ouput: ' + str(Solution().minDifference(case[0])) + '\n')