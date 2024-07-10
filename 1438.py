from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

if __name__ == '__main__':
    test_cases = ( ([8,2,4,7], 4, 2), ([10,1,2,4,7,2], 5, 4))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().longestSubarray(case[0], case[1])) + '\n')