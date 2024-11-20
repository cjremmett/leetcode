from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = []
        for i in range(0, len(nums)):
            if nums[i] % 2 == 1:
                odds.append(i)

        num_nice_subs = 0
        for i in range(0, len(odds) - k + 1):
            left_window_size = 0 
            if i == 0:
                left_window_size = odds[i]
            else:
                left_window_size = odds[i] - odds[i-1] - 1

            right_window_size = 0
            if i + k == len(odds):
                right_window_size = len(nums) - odds[i+k-1] - 1
            else:
                right_window_size = odds[i+k] - odds[i+k-1] - 1
            num_nice_subs += (left_window_size + 1) * (right_window_size + 1)

        return num_nice_subs


if __name__ == '__main__':
    test_cases = ( ([1,1,2,1,1], 3, 2), ([2,4,6], 1, 0), ([2,2,2,1,2,2,1,2,2,2], 2, 16))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().numberOfSubarrays(case[0], case[1])) + '\n')