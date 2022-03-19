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
    def isPalindrome(self, head: ListNode) -> bool:
        logger.debug('-' * 40)
        logger.debug(f'{head=}')
        if head is None:
            return True
        if head.next is None:
            return True

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
        second_half_i = half_len + 2 if len % 2 else half_len + 1

        # get head of second half
        i = 2
        second_half_head = head.next
        second_half_parent = head
        while i < second_half_i:
            next_head = second_half_head.next
            second_half_parent = second_half_head
            del second_half_head
            second_half_head = next_head
            i += 1
        logger.debug(f'{second_half_head=}')

        # reverse second half
        second_half_parent.next = self.reverseList(second_half_head)
        logger.debug(f'reversed second half {head=}, {second_half_parent.next=}')

        # compare left and right half
        i = 1
        left_node = head
        right_node = second_half_parent.next
        result = True
        while i <= half_len:
            if left_node.val != right_node.val:
                result = False
                break

            next_left = left_node.next
            del left_node
            left_node = next_left

            next_right = right_node.next
            del right_node
            right_node = next_right

            i += 1
        logger.debug(f'{result=}')

        # reconstruct origin linked-list
        second_half_parent.next = self.reverseList(second_half_parent.next)
        logger.debug(f'after reconstruction {head=}')

        return result

    def reverseList(self, head: ListNode) -> ListNode:
        # logger.debug('-' * 40)
        # logger.debug(f'{head=}')
        new_head = None
        next_node = head
        while next_node is not None:
            # logger.debug(f'{head=}, {next_node=}, {new_head=}')
            new_head_next = new_head
            del new_head
            new_head = ListNode(next_node.val, new_head_next)

            next_node_next = next_node.next
            del next_node
            next_node = next_node_next

        return new_head


def main():
    assert Solution().isPalindrome(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ) is False

    assert Solution().isPalindrome(
        ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    ) is True

    assert Solution().isPalindrome(
        ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    ) is True

    assert Solution().isPalindrome(
        ListNode(1, ListNode(2))
    ) is False

    assert Solution().isPalindrome(
        ListNode(1)
    ) is True

    assert Solution().isPalindrome(
        None
    ) is True


if __name__ == '__main__':
    main()
