from typing import List, Optional

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        if self.check_is_peak(left_mid, nums):
                return left_mid
        if self.check_is_peak(right_mid, nums):
            return right_mid

        while True:
            left_mid = (right_pointer - left_pointer) // 3
            right_mid = ((right_pointer - left_pointer) // 3) * 2
            if self.check_is_peak(left_mid, nums):
                return left_mid
            if self.check_is_peak(right_mid, nums):
                return right_mid

            if nums[left_mid] == nums[right_mid]:
                left_pointer, right_pointer = left_mid, right_mid
            elif nums[left_mid] > nums[right_mid]:
                right_pointer = left_mid
            else:
                left_pointer = right_mid


    def check_is_peak(self, index, nums):
        greater_than_left = True if (index == 0 or nums[index] > nums[index - 1]) else False
        greater_than_right = True if (index == len(nums) - 1 or nums[index] > nums[index + 1]) else False
        return True if greater_than_left and greater_than_right else False

if __name__ == '__main__':
    test_cases = ( ([1,2,3,1], [2]), ([1,2,1,3,5,6,4], [1, 5]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().findPeakElement(case[0])) + '\n')