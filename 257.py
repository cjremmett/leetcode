from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        else:
            return_list = []
            self.traverse_node(root, [str(root.val)], return_list)
            return return_list
        
    def traverse_node(self, node: TreeNode, history: List[str], return_list: List[str]) -> None:
        if node.left is None and node.right is None:
            if len(history) == 0:
                return_list.append([str(node.val)])
            else:
                for path in history:
                    return_list.append(path)
        else:
            if node.left:
                new_history = self.append_to_history(node.left.val, history)
                self.traverse_node(node.left, new_history, return_list)
            
            if node.right:
                new_history = self.append_to_history(node.right.val, history)
                self.traverse_node(node.right, new_history, return_list)

            
    def append_to_history(self, val: int, history: List[str]) -> List[str]:
        new_history = []
        for path in history:
            new_history.append(path + '->' + str(val))
        
        return new_history

if __name__ == '__main__':
    node5 = TreeNode(5, None, None)
    node3 = TreeNode(3, None, None)
    node2 = TreeNode(2, None, node5)
    node1 = TreeNode(1, node2, node3)
    print(Solution().binaryTreePaths(node1))