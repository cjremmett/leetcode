
from typing import List
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        points = sorted(points, key=lambda x: (x[0], -x[1]))
        for i in range(len(points)-1, -1, -1):
            lowest_y_matched = None
            for j in range(i-1, -1, -1):
                if points[j][0] <= points[i][0] and points[j][1] >= points[i][1]:
                    if lowest_y_matched == None or points[j][1] < lowest_y_matched:
                        lowest_y_matched = points[j][1]
                        count += 1
                    
        
        return count
    

if __name__ == '__main__':
    test_cases = ( ([[1,1],[2,2],[3,3]], 0), ([[6,2],[4,4],[2,6]], 2), ([[3,1],[1,3],[1,1]], 2), ([[0,1],[1,3],[6,1]], 2))
    for case in test_cases:
        print(f'Input: {case[0]}\nExpected output: {case[1]}\nActual output: {Solution().numberOfPairs(case[0])}\n')