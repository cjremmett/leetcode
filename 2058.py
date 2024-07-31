from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head == None:
            return [-1, -1]

        c_inds = []

        prev_node = None
        next_node = head.next
        i = 0
        while head:
            if prev_node != None and next_node != None:
                if prev_node.val < head.val and next_node.val < head.val:
                    c_inds.append(i)
                elif prev_node.val > head.val and next_node.val > head.val:
                    c_inds.append(i)
            
            i += 1
            prev_node = head
            head = head.next
            if head.next:
                next_node = head.next
            else:
                break

        if len(c_inds) < 2:
            return [-1, -1]
        else:
            c_max = c_inds[-1] - c_inds[0]
            c_min = c_max
            for i in range(0, len(c_inds) - 1):
                c_min = min(c_min, c_inds[i + 1] - c_inds[i])
            return [c_min, c_max]


if __name__ == '__main__':
    node6 = ListNode(2, None)
    node5 = ListNode(1, node6)
    node4 = ListNode(5, node5)
    node3 = ListNode(2, node4)
    node2 = ListNode(1, node3)
    node1 = ListNode(3, node2)
    node0 = ListNode(5, node1)
    print(Solution().nodesBetweenCriticalPoints(node0))