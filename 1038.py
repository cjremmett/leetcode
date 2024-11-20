# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ord_arr = []
        ord_dict = {}
        self.get_array(ord_arr, ord_dict, root)
        total = sum(ord_arr)
        ind_arr_val = [total]
        for i in range(1, len(ord_arr)):
            ind_arr_val.append(ind_arr_val[i-1] - ord_arr[i-1])
        
        self.add_greater(root, ord_dict, ind_arr_val)
        return root

    def add_greater(self, node, val_dict, index_values):
        if node:
            self.add_greater(node.left, val_dict, index_values)
            node.val = index_values[val_dict[node.val]]
            self.add_greater(node.right, val_dict, index_values)

    def get_array(self, array, ord_dict, node):
        if node:
            self.get_array(array, ord_dict, node.left)
            array.append(node.val)
            ord_dict[node.val] = len(array) - 1
            self.get_array(array, ord_dict, node.right)


def print_tree(node):
    if node:
        print_tree(node.left)
        print(node.val)
        print_tree(node.right)

if __name__ == '__main__':
    node0 = TreeNode(0, None, None)
    node3 = TreeNode(3, None, None)
    node2 = TreeNode(2, None, node3)
    node1 = TreeNode(1, node0, node2)

    node8 = TreeNode(8, None, None)
    node7 = TreeNode(7, None, node8)
    node5 = TreeNode(5, None, None)
    node6 = TreeNode(6, node5, node7)
    node4 = TreeNode(4, node1, node6)

    Solution().bstToGst(node4)

    print_tree(node4)
    
