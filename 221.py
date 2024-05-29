from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_size = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == '1':
                    matrix[i][j] = 1
                    max_size = 1
                else:
                    matrix[i][j] = 0

        for i in range(1, min(len(matrix), len(matrix[0]))):
            matrix_temp = [[0] * (len(matrix[0]) - 1) for _ in range(0, len(matrix) - 1)]
            for j in range(0, len(matrix_temp)):
                for k in range(0, len(matrix_temp[j])):
                    if matrix[j][k] == 1 and matrix[j+1][k] == 1 and matrix[j][k+1] == 1 and matrix[j+1][k+1] == 1:
                        matrix_temp[j][k] = 1
                        max_size = (i+1) ** 2
            
            matrix = matrix_temp

        return max_size

if __name__ == '__main__':
    test_cases = ( ([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]], 16), ([["0","1"],["1","0"]], 1), ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4), ([["0"]], 0))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().maximalSquare(case[0])) + '\n')