from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.return_list = []
        for i in range(0, len(candidates)):
            self.iterate_num([], candidates[i], 0, candidates[i:], target)
        return self.return_list

    def iterate_num(self, progress, to_add, sum, candidates, target):
        progress = progress + [to_add]
        sum += to_add
        
        if sum > target:
            return
        elif sum == target:
            self.return_list.append(progress)
        else:
            for i in range(0, len(candidates)):
                self.iterate_num(progress, candidates[i], sum, candidates[i:], target)
    
if __name__ == '__main__':
    test_cases = [ ([2,3,6,7], 7, [[2,2,3],[7]]), ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]), ([2], 1, []) ]
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected output: ' + str(case[2]) + '\nActual output: ' + str(Solution().combinationSum(case[0], case[1])) + '\n')