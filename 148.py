from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_node = head
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        values.sort()
        head = head_node
        for i in range(0, len(values)):
            head.val = values[i]
            head = head.next

        return head_node


def print_nodes(node):
    if node:
        print(node.val)
        print_nodes(node.next)


if __name__ == '__main__':
    node1 = ListNode(5, None)
    node2 = ListNode(8, node1)
    node3 = ListNode(2, node2)
    print_nodes(Solution().sortList(node3))