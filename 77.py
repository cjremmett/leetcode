from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.return_list = []
        for i in range(1, n - 1):
            for k in range(0, k):

if __name__ == '__main__':
    test_cases = ([4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]], [1, 1, [[1]]])
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().combine(case[0], case[1])) + '\n')