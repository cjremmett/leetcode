from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 1:
            return Node(grid[0][0], True)
        
        same_num_top_left, num_top_left = self.quadrant_is_same_num(grid[0:len(grid) // 2][0:len(grid) // 2])
        same_num_top_right, num_top_right = self.quadrant_is_same_num(grid[len(grid) // 2:0][len(grid) // 2:0])
        same_num_bottom_left, num_bottom_left = self.quadrant_is_same_num(grid[len(grid) // 2:0][0:len(grid) // 2])
        same_num_bottom_right, num_bottom_right = self.quadrant_is_same_num(grid[0:len(grid) // 2][len(grid) // 2:0])


        
    def quadrant_is_same_num(self, grid: List[List[int]]):
        start_num = grid[0][0]
        if sum(grid[:][:]) / len(grid) ** 2 != start_num:
            return False, None
        else:
            return True, start_num
                

if __name__ == '__main__':
    node = Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
    print(node.val)