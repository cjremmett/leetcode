from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        idx = {0: 0, 1: 0, 2: 0}

        for i in range(0, len(nums)):
            num = nums[-1]
            nums.pop()
            nums.insert(idx[num], num)
            for i in range(num, 3):
                idx[i] += 1
        

if __name__ == '__main__':
    test_cases = ( ([2,0,2,1,1,0], [0,0,1,1,2,2]), ([2,0,1], [0,1,2]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().sortColors(case[0])) + ' ' + str(case[0]) + '\n')