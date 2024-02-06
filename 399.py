from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        return [0.0]


if __name__ == '__main__':
    test_cases = (([[["a","b"],["b","c"]]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]], [6.00000,0.50000,-1.00000,1.00000,-1.00000]), ([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]], [3.75000,0.40000,5.00000,0.20000]))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + ' ' + str(case[2]) + '\nExpected Output: ' + str(case[3]) + '\nActual Output: ' + str(Solution().calcEquation(case[0], case[1], case[2])) + '\n')