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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_l1 = l1
        current_l2 = l2
        result_head = None
        result_tail = None
        while current_l1 or current_l2:
            if current_l1 and current_l2:
                if current_l1.val >= current_l2.val:
                    next_node = ListNode(current_l2.val)
                    current_l2 = current_l2.next
                else:
                    next_node = ListNode(current_l1.val)
                    current_l1 = current_l1.next

            elif current_l1:
                next_node = ListNode(current_l1.val)
                current_l1 = current_l1.next
            else: # current_l2
                next_node = ListNode(current_l2.val)
                current_l2 = current_l2.next

            if result_head is None:
                result_head = next_node
                result_tail = result_head
            else:
                result_tail.next = next_node
                del result_tail
                result_tail = next_node

        # logger.debug(f'return result_head={result_head}')
        return result_head


def main():
    assert str(Solution().mergeTwoLists(
        l1=ListNode(1, ListNode(2, ListNode(4))),
        l2=ListNode(1, ListNode(3, ListNode(4)))
    )) == str(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))))

    assert str(Solution().mergeTwoLists(
        l1=ListNode(5),
        l2=ListNode(5)
    )) == str(ListNode(5, ListNode(5)))

    assert str(Solution().mergeTwoLists(
        l1=ListNode(2),
        l2=ListNode(6, ListNode(9))
    )) == str(ListNode(2, ListNode(6, ListNode(9))))

    assert str(Solution().mergeTwoLists(
        l2=ListNode(6, ListNode(9)),
        l1=ListNode(2)
    )) == str(ListNode(2, ListNode(6, ListNode(9))))


if __name__ == '__main__':
    main()
