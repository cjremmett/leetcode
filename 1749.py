from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p = 0
        highest_seen = 0
        current_count_high = 0
        current_count_low = 0
        lowest_seen = 0

        while p < len(nums):
            current_count_high += nums[p]
            current_count_low += nums[p]
            if current_count_high > highest_seen:
                highest_seen = current_count_high

            if current_count_low < lowest_seen:
                lowest_seen = current_count_low

            if current_count_high < 0:
                current_count_high = 0

            if current_count_low > 0:
                current_count_low = 0

            p += 1

        return max(abs(lowest_seen), highest_seen)


if __name__ == '__main__':
    test_cases = [ [ [1,-3,2,3,-4], 5], [[2,-5,1,-4,3,-2], 8]]
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maxAbsoluteSum(case[0])) + '\n')
