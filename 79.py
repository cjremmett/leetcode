from typing import List
from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.positions_dict = defaultdict(set)
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                self.positions_dict[board[i][j]].add((i, j))

        for tup in self.positions_dict[word[0]]:
            
        
    def next_letter_iteration(self, word, pos_to_check):
        if pos_to_check == len(word):
            return True
        else:

        return True


if __name__ == '__main__':
    test_cases = ( ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED', True), ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE', True), ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB', False))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected Output: ' + str(case[2]) + '\nActual Output: ' + str(Solution().exist(case[0], case[1])) + '\n')