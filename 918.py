from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:      
        current_max = nums[0]
        best_max = nums[0]
        current_min = nums[0]
        best_min = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(current_max + num, num)
            best_max = max(best_max, current_max)
            current_min = min(current_min + num, num)
            best_min = min(best_min, current_min)
            sum += num

        return max(best_max, sum - best_min)

if __name__ == '__main__':
    test_cases = ( ([1,-2,3,-2], 3), ([-3,-2,-3], -2) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maxSubarraySumCircular(case[0])) + '\n')