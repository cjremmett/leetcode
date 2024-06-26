from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        target_num = 1
        num_patches = 0

        i = 0
        while target_num <= n:
            if i < len(nums) and nums[i] <= target_num:
                target_num += nums[i]
                i += 1
            else:
                num_patches += 1
                target_num += target_num

        return num_patches


if __name__ == '__main__':
    test_cases = ( ([1,3], 6, 1), ([1,5,10], 20, 2), ([1,2,2], 5, 0) )
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().minPatches(case[0], case[1])) + '\n')