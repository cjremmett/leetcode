from collections import deque

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def traverse_node(node):
    if node:
        traverse_node(node.left)
        print(node.val)
        traverse_node(node.right)

def level_order_traverse(node):
    queue = deque()
    queue.append(node)
    output = []
    while(len(queue) > 0):
        node = queue.popleft()
        output.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    for i in range(len(output) - 1, -1, -1):
        print(output[i])

if __name__ == '__main__':
    node7 = Node(7, None, None)
    node6 = Node(6, None, None)
    node5 = Node(5, None, None)
    node4 = Node(4, None, None)

    node3 = Node(3, node6, node7)
    node2 = Node(2, node4, node5)

    node1 = Node(1, node2, node3)

    level_order_traverse(node1)
