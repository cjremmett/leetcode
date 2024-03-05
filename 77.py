from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.return_list = set()
        for i in range(1, n + 1):
            self.list_builder(set(), i, n, k)
        
        return self.return_list

    def list_builder(self, progress, num_to_add, end, k):
        if num_to_add in progress:
            return
        else:
            progress.add(num_to_add)
            if len(progress) == k:
                self.return_list.add(frozenset(progress))
                return

            for i in range(num_to_add, end + 1):
                self.list_builder(progress.copy(), i, end, k)

if __name__ == '__main__':
    test_cases = ( [3, 3, [1, 2, 3]], [1, 1, [[1]]], [4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]])
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().combine(case[0], case[1])) + '\n')