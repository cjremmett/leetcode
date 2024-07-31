from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        windows = []
        window = 0
        head = head.next
        while head:
            if head.val == 0:
                windows.append(window)
                window = 0
                head = head.next
            else:
                window += head.val
                head = head.next

        if len(windows) == 0:
            return None
        else:
            root = ListNode(windows[0])
            node = root
            for i in range(1, len(windows)):
                node.next = ListNode(windows[i])
                node = node.next

            return root


if __name__ == '__main__':
    node5 = ListNode(0, None)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(0, node3)
    node1 = ListNode(1, node2)
    node0 = ListNode(0, node1)
    root = Solution().mergeNodes(node0)
    while root:
        print(root.val)
        root = root.next