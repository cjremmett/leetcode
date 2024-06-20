from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        increment = 0
        prev_num = -1
        
        for num in nums:
            if num <= prev_num:
                increment += prev_num - num + 1
                prev_num = num + (prev_num - num) + 1
            else:
                prev_num = num

        return increment


if __name__ == '__main__':
    test_cases = ( ([1,2,2], 1), ([3,2,1,2,1,7], 6))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minIncrementForUnique(case[0])) + '\n')