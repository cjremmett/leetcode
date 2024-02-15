from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        return -1


if __name__ == '__main__':
    test_cases = (([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]], 4), ([[-1,-1],[-1,3]], 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected Output: ' + str(case[1]) + '\nActual Output: ' + str(Solution().snakesAndLadders(case[0])) + '\n')