from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.return_set = set()
        self.nums = set(range(1, n + 1))

    
    def iterate(self, progress_so_far, iteration_count):
        if iteration_count >= k:
            self.return_set.add(tuple(progress_so_far))

if __name__ == '__main__':
    test_cases = ([4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]], [1, 1, [[1]]])
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().combine(case[0], case[1])) + '\n')