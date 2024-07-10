from typing import List
import bisect

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        max_seen = 1
        left = 0
        right = 0
        ordered_list = []
        bisect.insort_left(ordered_list, nums[left])

        while right < len(nums):
            if ordered_list[-1] - ordered_list[0] <= limit:
                if right - left + 1 > max_seen:
                    max_seen = right - left + 1
                
                right += 1
                if right < len(nums):
                    bisect.insort_left(ordered_list, nums[right])
            elif ordered_list[-1] - ordered_list[0] > limit:
                ordered_list.remove(nums[left])
                left += 1

        return max_seen


if __name__ == '__main__':
    test_cases = ( ([8,2,4,7], 4, 2), ([10,1,2,4,7,2], 5, 4))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().longestSubarray(case[0], case[1])) + '\n')