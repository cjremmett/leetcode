from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0
        
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = [1]
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                segmax = []
                if j - 1 >= 0 and obstacleGrid[i][j-1] != 1:
                    segmax.append([obstacleGrid[i][j-1][0]])
                if i - 1 >= 0 and obstacleGrid[i-1][j] != 1:
                    segmax.append([obstacleGrid[i-1][j][0]])
                
                if len(segmax) == 0:
                    obstacleGrid[i][j] = [0]
                elif len(segmax) == 1:
                    obstacleGrid[i][j] = segmax[0]
                else:
                    obstacleGrid[i][j] = [segmax[0][0] + segmax[1][0]]

        return obstacleGrid[-1][-1][0]
    

if __name__ == '__main__':
    test_cases = ( ([[0,0,0],[0,1,0],[0,0,0]], 2), ([[0,1],[0,0]], 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().uniquePathsWithObstacles(case[0])) + '\n')