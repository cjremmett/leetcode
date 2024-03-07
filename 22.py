from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.return_set = set()
        self.iterate_parenthesis([], 0, 1, n)
        return self.return_set

    def iterate_parenthesis(self, progress, insert_pos_one, insert_pos_two, n):
        progress.insert(insert_pos_one, '(')
        progress.insert(insert_pos_two, ')')
        if len(progress) >= n * 2:
            self.return_set.add(''.join(progress))
        else:
            for i in range(0, len(progress)):
                for j in range(i + 1, len(progress) + 1):
                    self.iterate_parenthesis(progress[:], i, j, n)
    

if __name__ == '__main__':
    test_cases = ( [7, ['']], [3, ["((()))","(()())","(())()","()(())","()()()"]], [1, ["()"]])
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected Output: ' + str(case[1]) + '\nActual Output: ' + str(Solution().generateParenthesis(case[0])) + '\n')