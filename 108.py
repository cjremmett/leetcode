from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root_node = TreeNode

    def create_subtree(self, nums, node):
        if len(nums) == 0:
            return
        
        left_node = TreeNode(nums[len(nums) // 2])
        node.left = left_node
        left_nums = nums[0:len(nums) // 2]
        nums.pop(len(nums) // 2)
        create_subtree(left_nums, left_node)

        if len(nums) == 0:
            return

        right_node = TreeNode(nums[len(nums) // 2])
        node.right = right_node
        right_nums = nums[(len(nums) // 2) + 1:]
        nums.pop(len(nums) // 2)
        create_subtree(right_nums, right_node)



if __name__ == '__main__':
    node = Solution().sortedArrayToBST([-10,-3,0,5,9])