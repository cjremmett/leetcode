# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder_array = []
        self.load_array(inorder_array, root)
        root_index = len(inorder_array) // 2

        left_node = None
        right_node = None

        prev_node = None
        for i in range(0, root_index):
            new_node = TreeNode(inorder_array[i], None, None)
            if prev_node:
                new_node.left = prev_node
            prev_node = new_node
        left_node = prev_node

        prev_node = None
        for i in reversed(range(root_index + 1, len(inorder_array))):
            new_node = TreeNode(inorder_array[i], None, None)
            if prev_node:
                new_node.right = prev_node
            prev_node = new_node
        right_node = prev_node

        return TreeNode(inorder_array[root_index], left_node, right_node)


    def load_array(self, inorder_array, node):
        if node:
            self.load_array(inorder_array, node.left)
            inorder_array.append(node.val)
            self.load_array(inorder_array, node.right)


def inorder_print(node):
    if node:
        inorder_print(node.left)
        print(node.val)
        inorder_print(node.right)

def preorder_print(node):
    if node:
        print(node.val)
        preorder_print(node.left)
        preorder_print(node.right)

if __name__ == '__main__':
    node4 = TreeNode(4, None, None)
    node3 = TreeNode(3, None, node4)
    node2 = TreeNode(2, None, node3)
    node1 = TreeNode(1, None, node2)
    inorder_print(node1)
    print(' ')
    preorder_print(node1)
    root = Solution().balanceBST(node1)
    print(' ')
    inorder_print(root)
    print(' ')
    preorder_print(root)