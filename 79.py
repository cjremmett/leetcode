from typing import List
from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.positions_dict = defaultdict(set)
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                self.positions_dict[board[i][j]].add((i, j))

        for tup in self.positions_dict[word[0]]:
            result = self.next_letter_iteration((tup[0], tup[1]), word, 1, set())
            if result == True:
                return True
        
        return False
        
    def next_letter_iteration(self, pos, word, count, already_seen):
        if count == len(word):
            return True
        
        if (pos[0] - 1, pos[1]) in self.positions_dict[word[count]] and (pos[0] - 1, pos[1]) not in already_seen:
            up_seen = already_seen.copy()
            up_seen.add((pos[0] - 1, pos[1]))
            up = self.next_letter_iteration((pos[0] - 1, pos[1]), word, count + 1, up_seen)
            if up == True:
                return True

        if (pos[0] + 1, pos[1]) in self.positions_dict[word[count]] and (pos[0] + 1, pos[1]) not in already_seen:
            down_seen = already_seen.copy()
            down_seen.add((pos[0] - 1, pos[1]))
            down = self.next_letter_iteration((pos[0] + 1, pos[1]), word, count + 1, down_seen)
            if down == True:
                return True

        if (pos[0], pos[1] - 1) in self.positions_dict[word[count]] and (pos[0], pos[1] - 1) not in already_seen:
            left_seen = already_seen.copy()
            left_seen.add((pos[0] - 1, pos[1]))
            left = self.next_letter_iteration((pos[0], pos[1] - 1), word, count + 1, left_seen)
            if left == True:
                return True

        if (pos[0], pos[1] + 1) in self.positions_dict[word[count]] and (pos[0], pos[1] + 1) not in already_seen:
            right_seen = already_seen.copy()
            right_seen.add((pos[0] - 1, pos[1]))
            right = self.next_letter_iteration((pos[0], pos[1] + 1), word, count + 1, right_seen)
            if right == True:
                return True
            
        return False
        



if __name__ == '__main__':
    test_cases = ( ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB', False), ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED', True), ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE', True))
    for case in test_cases:
        print('Input: ' + str(case[0]) + ' ' + str(case[1]) + '\nExpected Output: ' + str(case[2]) + '\nActual Output: ' + str(Solution().exist(case[0], case[1])) + '\n')