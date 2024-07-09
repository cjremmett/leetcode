from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice_subs = 0
        left = 0
        right = -1
        num_odd = 0
        for i in range(0, len(nums)):
            right += 1
            if nums[right] % 2 == 1:
                num_odd += 1

            while num_odd > k:
                if nums[left] % 2 == 1:
                    num_odd -= 1
                left -= 1

            if num_odd == k:
                nice_subs += 1

        return nice_subs


if __name__ == '__main__':
    test_cases = ( ([1,1,2,1,1], 3, 2), ([2,4,6], 1, 0), ([2,2,2,1,2,2,1,2,2,2], 2, 16))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().numberOfSubarrays(case[0], case[1])) + '\n')