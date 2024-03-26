from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        root_node = TreeNode(nums[len(nums) // 2])
        root_node.left = self.sortedArrayToBST(nums[0:len(nums) // 2])
        root_node.right = self.sortedArrayToBST(nums[(len(nums) // 2) + 1:])
        return root_node
        
def inorder_traverse(node):
    if node.left:
        inorder_traverse(node.left)

    print(node.val)

    if node.right:
        inorder_traverse(node.right)


if __name__ == '__main__':
    node = Solution().sortedArrayToBST([-10,-3,0,5,9])
    inorder_traverse(node)
    print('\n')
    node = Solution().sortedArrayToBST([-1,0,1,2])
    inorder_traverse(node)