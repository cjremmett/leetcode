from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        right = k - 1
        max_sum = 0
        current_window_sum = sum(nums[0:k])
        current_window_counts = defaultdict(int)
        for num in nums[0:k]:
            current_window_counts[num] += 1

        if max(list(current_window_counts.values())) <= 1:
            max_sum = current_window_sum

        while right < len(nums) - 1:
            current_window_sum -= nums[left]
            current_window_counts[nums[left]] -= 1
            left += 1

            right += 1
            current_window_sum += nums[right]
            current_window_counts[nums[right]] += 1

            if max(list(current_window_counts.values())) <= 1 and current_window_sum > max_sum:
                max_sum = current_window_sum

        return max_sum
    

if __name__ == '__main__':
    test_cases = [ [[1,5,4,2,9,9,9], 3, 15], [[4,4,4], 3, 0]]
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().maximumSubarraySum(case[0], case[1])) + '\n')