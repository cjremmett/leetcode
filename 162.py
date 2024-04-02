from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while True:
            mid_index = (right_pointer - left_pointer) // 2
            mid_greater_than_left = True if (mid_index == 0 or nums[mid_index] > nums[mid_index - 1]) else False
            mid_greater_than_right = True if (mid_index == len(nums) - 1 or nums[mid_index] > nums[mid_index + 1]) else False
            if mid_greater_than_left and mid_greater_than_right:
                return mid_index
            else:
                if nums[left_pointer] > nums[right_pointer]:
                    right_pointer = mid_index
                else:
                    left_pointer = mid_index
    

if __name__ == '__main__':
    test_cases = ( ([1,2,3,1], [2]), ([1,2,1,3,5,6,4], [1, 5]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().findPeakElement(case[0])) + '\n')