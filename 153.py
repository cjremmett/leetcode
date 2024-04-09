from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:                
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        while True:
            mid = left + ((right - left) // 2)
            if self.check_is_min(mid, nums):
                return nums[mid]
            elif nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

            
    def check_is_min(self, index, nums):
        if nums[index] < nums[index - 1]:
            return True
        else:
            return False
    

if __name__ == '__main__':
    test_cases = ( [[5,1,2,3,4], 1], [[3,1,2], 1], [[3,4,5,1,2], 1], [[4,5,6,7,0,1,2], 0], [[11,13,15,17], 11])
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().findMin(case[0])) + '\n')