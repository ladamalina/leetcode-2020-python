import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        next_str = f' -> {self.next.__repr__()}' if self.next else ''
        return f'{self.val}{next_str}'


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        logger.debug('-' * 40)
        logger.debug(f'{head=}')
        if head.next is None:
            return head

        # get length
        len = 2
        tail = head.next
        while tail.next is not None:
            next_tail = tail.next
            del tail
            tail = next_tail
            len += 1
        logger.debug(f'{len=}')
        half_len = len // 2
        second_half_i = half_len + 1 if len % 2 else half_len + 1

        # get head of second half
        i = 2
        second_half_head = head.next
        while i < second_half_i:
            next_head = second_half_head.next
            del second_half_head
            second_half_head = next_head
            i += 1
        logger.debug(f'{second_half_head=}')

        return second_half_head


def main():
    assert str(Solution().middleNode(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    )) == str(ListNode(3, ListNode(4, ListNode(5))))

    assert str(Solution().middleNode(
        ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    )) == str(ListNode(2, ListNode(1)))

    assert str(Solution().middleNode(
        ListNode(1, ListNode(2))
    )) == str(ListNode(2))

    assert str(Solution().middleNode(
        ListNode(1)
    )) == str(ListNode(1))


if __name__ == '__main__':
    main()
