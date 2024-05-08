from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        


if __name__ == '__main__':
    test_cases = ( ([1,2,5], 11, 3), ([2], 3, -1), ([1], 0, 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ', ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().coinChange(case[0], case[1])) + '\n')