from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current_node_index = 0
        current_node = head
        one_behind_deletion_node = head
        while current_node.next:
            current_node_index += 1
            if current_node_index % 2 == 1 and current_node_index >= 3:
                one_behind_deletion_node = one_behind_deletion_node.next
            current_node = current_node.next

        match current_node_index:
            case 0:
                return None
            case 1:
                one_behind_deletion_node.next = None
                return one_behind_deletion_node
            case _:
                one_behind_deletion_node.next = one_behind_deletion_node.next.next
                return head


if __name__ == '__main__':
    node2: ListNode = ListNode(2, None)
    node1: ListNode = ListNode(1, node2)
    node0: ListNode = ListNode(0, node1)
    head = Solution().deleteMiddle(node0)
    print(head.next if head else "None!")

        