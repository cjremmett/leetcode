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
            return Node(grid[0][0], True, None, None, None, None)
        
        root_same, same_num = self.quadrant_is_same_num(grid)
        if root_same == True:
            return Node(same_num, True, None, None, None, None)
        else:
            root_node = Node(1, False, None, None, None, None)
            self.recurse(grid, root_node)
            return root_node
        
        
    def recurse(self, grid, node):
        
        same_num_top_left, num_top_left = self.quadrant_is_same_num([(grid[i])[0:len(grid) // 2] for i in range(0, len(grid) // 2)])
        same_num_top_right, num_top_right = self.quadrant_is_same_num([(grid[i])[len(grid) // 2:] for i in range(0, len(grid) // 2)])
        same_num_bottom_left, num_bottom_left = self.quadrant_is_same_num([(grid[i])[0:len(grid) // 2] for i in range(len(grid) // 2, len(grid))])
        same_num_bottom_right, num_bottom_right = self.quadrant_is_same_num([(grid[i])[len(grid) // 2:] for i in range(len(grid) // 2, len(grid))])

        if same_num_top_left == True:
            node.topLeft = Node(num_top_left, True, None, None, None, None)
        else:
            node.topLeft = Node(1, False, None, None, None, None)
            self.recurse([(grid[i])[0:len(grid) // 2] for i in range(0, len(grid) // 2)], node.topLeft)

        if same_num_top_right == True:
            node.topRight = Node(num_top_right, True, None, None, None, None)
        else:
            node.topRight = Node(1, False, None, None, None, None)
            self.recurse([(grid[i])[len(grid) // 2:] for i in range(0, len(grid) // 2)], node.topRight)

        if same_num_bottom_left == True:
            node.bottomLeft = Node(num_bottom_left, True, None, None, None, None)
        else:
            node.bottomLeft = Node(1, False, None, None, None, None)
            self.recurse([(grid[i])[0:len(grid) // 2] for i in range(len(grid) // 2, len(grid))], node.bottomLeft)

        if same_num_bottom_right == True:
            node.bottomRight = Node(num_bottom_right, True, None, None, None, None)
        else:
            node.bottomRight = Node(1, False, None, None, None, None)
            self.recurse([(grid[i])[len(grid) // 2:] for i in range(len(grid) // 2, len(grid))], node.bottomRight)
        
    def quadrant_is_same_num(self, grid: List[List[int]]):
        if len(grid) <= 0:
            return False, None
        
        start_num = grid[0][0]
        grid_total = 0
        for row in grid:
            grid_total += sum(row)

        if grid_total / len(grid) ** 2 != start_num:
            return False, None
        else:
            return True, start_num
                

if __name__ == '__main__':
    #node = Solution().construct([[1,1],[1,1]])
    node = Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
    print(node.val)
    print(node.isLeaf)
    print(node.topLeft.val)
    print(node.topLeft.isLeaf)
    print(node.topRight.val)
    print(node.topRight.isLeaf)

    print(node.topRight.topLeft.val)
    print(node.topRight.topLeft.isLeaf)
    print(node.topRight.topRight.val)
    print(node.topRight.topRight.isLeaf)
    print(node.topRight.bottomLeft.val)
    print(node.topRight.bottomLeft.isLeaf)
    print(node.topRight.bottomRight.val)
    print(node.topRight.bottomRight.isLeaf)

    print(node.bottomLeft.val)
    print(node.bottomLeft.isLeaf)
    print(node.bottomRight.val)
    print(node.bottomRight.isLeaf)