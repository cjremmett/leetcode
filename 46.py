from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.return_list = []
        self.generate_permutations(list(), set(nums))
        return self.return_list

    def generate_permutations(self, progress, nums_to_insert):
        if len(nums_to_insert) == 0:
            self.return_list.append(progress)
        else:
            for num in nums_to_insert:
                self.generate_permutations(progress + [num], nums_to_insert - {num})

if __name__ == '__main__':
    test_cases = [ [ [1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] ], [ [0,1], [[0,1],[1,0]] ], [ [1], [[1]]] ]
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().permute(case[0])) + '\n')