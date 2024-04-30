from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        
        return result
    

if __name__ == '__main__':
    test_cases = ( ([2,2,1], 1), ([4,1,2,1,2], 4), ([1], 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().singleNumber(case[0])) + '\n')