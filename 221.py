from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        dp.append(matrix)
        for i in range(1, min(len(matrix), len(matrix[i]))):
            dp_temp = [['0'] * (len(matrix) - 1) for _ in range(0, len(matrix[0] - 1))]
            dp.append(dp_temp)

        return dp

if __name__ == '__main__':
    test_cases = ( ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4), ([["0","1"],["1","0"]], 1), ([["0"]], 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maximalSquare(case[1])) + '\n')