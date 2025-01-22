from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        water_cells = []
        for i in range(0, len(isWater)):
            for j in range(0, len(isWater[0])):
                if isWater[i][j] == 0:
                    isWater[i][j] = 1
                else:
                    water_cells.append((i, j))
                    isWater[i][j] = 0

        for i in range(0, len(isWater)):
            for j in range(0, len(isWater[0])):
                if isWater[i][j] == 1:
                    isWater[i][j] = self.jumps_to_water([i, j], water_cells)

        return isWater


    def jumps_to_water(self, cell, water_cells):
        min_jumps = None
        for water_cell in water_cells:
            x_jumps = abs(cell[1] - water_cell[1])
            y_jumps = abs(cell[0] - water_cell[0])
            if min_jumps is None or x_jumps + y_jumps < min_jumps:
                min_jumps = x_jumps + y_jumps

        return min_jumps
    


if __name__ == '__main__':
    test_cases = [ [[[0,1],[0,0]], [[1,0],[2,1]]], [[[0,0,1],[1,0,0],[0,0,0]], [[1,1,0],[0,1,1],[1,2,2]]] ]
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().highestPeak(case[0])) + '\n')