from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=self.sort_func, reverse=True)
        return intervals

    
    def sort_func(element1, element2):
        if element1[0] != element2[0]:
            return element[0]
        else:
            return element[1]
        
    

if __name__ == '__main__':
    test_cases = [([[1,4],[3,6],[2,8]], 2), ([[1,4],[2,3]], 1)]
    for case in test_cases:
        print(f'Input: {case[0]}')
        print(f'Expected result: {case[1]}')
        print(f'Actual result: {Solution().removeCoveredIntervals(case[0])}')