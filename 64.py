from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid) + len(grid[0]) - 1):
            for j in range(0, len(grid)):
                if i - j >= 0 and i - j < len(grid[0]):
                    segmin = set()
                    if j - 1 >= 0:
                        segmin.add(grid[j][i-j] + grid[j-1][i-j])
                    if i-j - 1 >= 0:
                        segmin.add(grid[j][i-j] + grid[j][i-j-1])
                    grid[j][i-j] = min(segmin)

        return grid[-1][-1]    

if __name__ == '__main__':
    test_cases = ( ([[1,2,3],[4,5,6]], 12), ([[1,3,1],[1,5,1],[4,2,1]], 7))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minPathSum(case[0])) + '\n')