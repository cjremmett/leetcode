from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

if __name__ == '__main__':
    test_cases = (['23', ["ad","ae","af","bd","be","bf","cd","ce","cf"]], ['', []], ['2', ["a","b","c"]])
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected output: ' + str(case[1]) + '\nActual output: ' + str(Solution().letterCombinations(case[0])))