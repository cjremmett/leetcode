from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                possible_vals = set()
                if j > 0:
                    possible_vals.add(triangle[i-1][j-1] + triangle[i][j])
                if j < len(triangle[i-1]):
                    possible_vals.add(triangle[i-1][j] + triangle[i][j])
                triangle[i][j] = min(possible_vals)

        return min(triangle[-1])
    
if __name__ == '__main__':
    test_cases = ( ([[-10]], -10), ([[2],[3,4],[6,5,7],[4,1,8,3]], 11))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().minimumTotal(case[0])) + '\n')