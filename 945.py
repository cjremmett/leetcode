from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        increment = 0
        prev_num = 0

        


if __name__ == '__main__':
    test_cases = ( ([1,2,2], 1), ([3,2,1,2,1,7], 6))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minIncrementForUnique(case[0])) + '\n')