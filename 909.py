from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # reorder board to make it easier to solve
        direction = 'right'
        self.list_board = []
        for i in reversed(range(0, len(board))):
            if direction == 'right':
                self.list_board += board[i]
                direction = 'left'
            else:
                self.list_board += board[i][::-1]
                direction = 'right'
        
        self.count = 0
        self.previous_buffers = set()
        self.buffer = set()
        self.buffer.add(0)

        while True:
            # increment step count and load previous buffer
            self.count += 1
            self.previous_buffer = self.buffer.copy()
            self.previous_buffers.add(tuple(self.buffer))
            self.buffer = set()

            # for each pointer location in buffer, step through all six actions, and return count if we're on the last index
            for index in self.previous_buffer:
                for i in range(1, 7):
                    if index + i >= len(self.list_board):
                        continue
                    elif self.list_board[index + i] != -1:
                        self.buffer.add(self.list_board[index + i] - 1)
                    else:
                        self.buffer.add(index + i)

            # check if we found the end
            if len(self.list_board) - 1 in self.buffer:
                return self.count
            
            # check for infinite loop
            if tuple(self.buffer) in self.previous_buffers:
                return -1


if __name__ == '__main__':
    test_cases = (([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[1,1,1,-1,13,-1],[1,1,1,1,1,8],[-1,8,8,8,8,8]], -1), ([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]], 4), ([[-1,-1],[-1,3]], 1))
    for case in test_cases:
        print('Input: ' + str(case[0]) + '\nExpected Output: ' + str(case[1]) + '\nActual Output: ' + str(Solution().snakesAndLadders(case[0])) + '\n')