from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        index = {}
        for i in range(1, len(nums)):
            index[i] = sum(nums[0:i])
        


if __name__ == '__main__':
    test_cases = ( ([23,2,4,6,7], 6, True), ([23,2,6,4,7], 6, True), ([23,2,6,4,7], 13, False))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().checkSubarraySum(case[0], case[1])) + '\n')