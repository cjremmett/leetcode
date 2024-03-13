from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.return_set = set('()')
        for i in range(1, n):
            self.iterate_parenthesis()
        return self.return_set

    def iterate_parenthesis(self):
        results = self.return_set.copy()
        for result in results:
            self.return_set.add('()' + result)
            self.return_set.add(result + '()')
            self.return_set.add('(' + result + ')')

if __name__ == '__main__':
    test_cases = ( [3, ["((()))","(()())","(())()","()(())","()()()"]], [2, ['()()', '(())']], [1, ["()"]])
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected Output: ' + str(case[1]) + '\nActual Output: ' + str(Solution().generateParenthesis(case[0])) + '\n')