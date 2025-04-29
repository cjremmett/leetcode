from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count_solutions = 0
        lp = 0
        rp = 2
        while rp < len(nums):
            if nums[lp] + nums[rp] == nums[lp+1] / 2:
                count_solutions += 1
            lp += 1
            rp += 1
        
        return count_solutions

if __name__ == '__main__':
    test_cases = ( ([1,2,1,4,1], 1), ([1,1,1], 0), ([2,-7,-6], 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().countSubarrays(case[0])) + '\n')