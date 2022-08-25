"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """"""

    # All the solutions are (modifications of the solutions) from
    # https://github.com/samyak1409/DSA/blob/main/02%29%20Linked%20List/026%29%20Middle%20of%20the%20Linked%20List.py.

    # 1) Optimal (Slow and Fast Pointer): TC = O(n); SC = O(1)
    # https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/discuss/1612140/One-Pass-Slow-and-Fast

    if not head.next:  # edge case: if only one node is there in the LL
        return None  # it should be deleted and None will be returned

    slow, fast = head, head.next.next  # start slow with head and fast two ahead of slow
    # because as we have to delete the mid. node, we need to stop 1 node before the mid. node
    # Traversing till the node before mid. node:
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next  # changing ptrs so that mid. node is deleted
    return head