import logging
import math
import sys
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        current = head
        last_seen_odd = head
        first_seen_even = head.next
        prev = None
        while current and current.next:
            if current is head:
                prev = current.next
                current = current.next.next
                continue

            current_next = current.next
            last_seen_odd.next = current
            last_seen_odd.next.next = first_seen_even
            prev.next = current_next
            last_seen_odd = last_seen_odd.next
            current = current_next.next if current_next else None
            prev = current_next

        if current:  # and current.next is none
            last_seen_odd.next = current
            last_seen_odd.next.next = first_seen_even
            prev.next = None

        return head


def main():
    pass


if __name__ == '__main__':
    main()
