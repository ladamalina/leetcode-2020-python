import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        next_str = f' -> {self.next.__repr__()}' if self.next else ''
        return f'{self.val}{next_str}'


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        link1 = head
        link2 = head
        while True:
            # move link1 1 step forward
            if link1.next is None:
                return False
            link1_next = link1.next
            del link1
            link1 = link1_next

            #move link2 2 steps forward
            if link2.next is None or link2.next.next is None:
                return False
            link2_next = link2.next.next
            del link2
            link2 = link2_next

            if link1 == link2:
                return True


def main():
    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    node4 = ListNode(9)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    assert Solution().hasCycle(head) is True

    head = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    node4 = ListNode(9)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    assert Solution().hasCycle(head) is False


if __name__ == '__main__':
    main()
