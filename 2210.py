from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        num_found = 0

        if len(nums) < 3:
            return 0

        dd = [nums[0]]
        for i in range(1, len(nums)):
            if dd[-1] != nums[i]:
                dd.append(nums[i])

        for i in range(1, len(dd) - 1):
            if dd[i-1] > dd[i] and dd[i+1] > dd[i]:
                num_found += 1
            elif dd[i-1] < dd[i] and dd[i+1] < dd[i]:
                num_found += 1

        return num_found



if __name__ == '__main__':
    test_cases = [ [[2,4,1,1,6,5], 3], [[6,6,5,5,4,1], 0] ]
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().countHillValley(case[0])) + '\n')