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
    def reverseList(self, head: ListNode) -> ListNode:
        logger.debug('-' * 40)
        logger.debug(f'{head=}')
        new_head = None
        next_node = head
        while next_node is not None:
            logger.debug(f'{head=}, {next_node=}, {new_head=}')
            new_head_next = new_head
            del new_head
            new_head = ListNode(next_node.val, new_head_next)

            next_node_next = next_node.next
            del next_node
            next_node = next_node_next

        return new_head



def main():
    assert str(Solution().reverseList(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    )) == str(ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))))

    assert str(Solution().reverseList(
        ListNode(1, ListNode(2))
    )) == str(ListNode(2, ListNode(1)))

    assert str(Solution().reverseList(
        ListNode(1)
    )) == str(ListNode(1))


if __name__ == '__main__':
    main()
