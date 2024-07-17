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

        return self.return_next_node(inorder_array)


    def load_array(self, inorder_array, node):
        if node:
            self.load_array(inorder_array, node.left)
            inorder_array.append(node.val)
            self.load_array(inorder_array, node.right)

    def return_next_node(self, values_to_create):
        if len(values_to_create) == 0:
            return None
        elif len(values_to_create) == 1:
            return TreeNode(values_to_create[0], None, None)
        else:
            mid = len(values_to_create) // 2
            left = self.return_next_node(values_to_create[0:mid])
            right = self.return_next_node(values_to_create[mid+1:])
            return TreeNode(values_to_create[mid], left, right)


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
    node6 = TreeNode(6, None, None)
    node5 = TreeNode(5, None, node6)
    node4 = TreeNode(4, None, node5)
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