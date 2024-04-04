from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        instance_index = self.get_index_of_target(nums, target)
        if instance_index == -1:
            return [-1,-1]
        
        left_bound = self.get_left_bound(nums, target, instance_index)
        right_bound = self.get_right_bound(nums, target, instance_index)
        return [left_bound, right_bound]
        

    def get_left_bound(self, nums, target, instance):
        left_pointer = 0
        right_pointer = instance - 1
        while True:
            if nums[left_pointer] == target and (left_pointer - 1 == -1 or nums[left_pointer - 1] < target):
                return left_pointer
            elif nums[right_pointer] == target and (right_pointer - 1 == -1 or nums[right_pointer - 1] < target):
                return right_pointer
            
            mid_pointer = left_pointer + ((right_pointer - left_pointer) // 2)
            if nums[mid_pointer] == target and (mid_pointer - 1 == -1 or nums[mid_pointer - 1] < target):
                return mid_pointer
            elif nums[mid_pointer] == target:
                right_pointer = mid_pointer - 1
            else:
                left_pointer = mid_pointer + 1

    def get_right_bound(self, nums, target, instance):
        left_pointer = instance
        right_pointer = len(nums) - 1
        while True:
            if nums[left_pointer] == target and (left_pointer + 1 == len(nums) or nums[left_pointer + 1] > target):
                return left_pointer
            elif nums[right_pointer] == target and (right_pointer + 1 == len(nums) or nums[right_pointer + 1] > target):
                return right_pointer
            
            mid_pointer = left_pointer + ((right_pointer - left_pointer) // 2)
            if nums[mid_pointer] == target and (mid_pointer + 1 == len(nums) or nums[mid_pointer + 1] > target):
                return mid_pointer
            elif nums[mid_pointer] > target:
                right_pointer = mid_pointer - 1
            else:
                left_pointer = mid_pointer + 1
    
    def get_index_of_target(self, nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1
        while True:
            if left_pointer > right_pointer or right_pointer < left_pointer or left_pointer >= len(nums) or right_pointer < 0:
                return -1
            
            if nums[left_pointer] == target:
                return left_pointer
            elif nums[right_pointer] == target:
                return right_pointer
            
            mid_pointer = left_pointer + ((right_pointer - left_pointer) // 2)
            if nums[mid_pointer] == target:
                return mid_pointer
            elif nums[mid_pointer] > target:
                right_pointer = mid_pointer - 1
            else:
                left_pointer = mid_pointer + 1


if __name__ == '__main__':
    test_cases = ( ([2,2], 3, [-1,-1]), ([1], 0, [-1,-1]), ([5,7,7,8,8,10], 8, [3,4]), ([5,7,7,8,8,10], 6, [-1,-1]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().searchRange(case[0], case[1])) + '\n')