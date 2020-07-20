import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = self.list_len(headA)
        len_b = self.list_len(headB)

        max_head = headA if len_a > len_b else headB
        min_head = headA if max_head is headB else headB

        len_diff = max(len_a, len_b) - min(len_a, len_b)
        for i in range(0, len_diff):
            max_head = max_head.next

        while max_head is not min_head and max_head.next:
            max_head = max_head.next
            min_head = min_head.next

        return max_head if max_head is min_head else None


    def list_len(self, l: ListNode) -> int:
        if l is None:
            return 0
        length = 1
        head = l
        while head.next:
            length += 1
            head = head.next

        return length


def main():
    pass


if __name__ == '__main__':
    main()
