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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        main_head = None
        current_prev = None
        current_head = head
        while current_head:
            current_next = current_head.next
            logger.debug(f'head={head}, BEFORE SWAP: current_head={current_head}, current_next={current_next}')
            if not current_next:
                if not main_head:
                    main_head = current_head
                current_head = None
                continue

            logger.debug(f'BEFORE SWAP: current_prev={current_prev}')
            if current_prev:
                del current_prev.next
                current_prev.next = current_next
            else:
                current_prev = current_head

            del current_head.next
            current_head.next = current_next.next
            del current_next.next
            current_next.next = current_head
            logger.debug(f'AFTER SWAP: current_head={current_head}')

            next_head = current_head.next
            del current_head
            current_head = next_head
            logger.debug(f'AFTER SWAP: current_head={current_head}')

            logger.debug(f'AFTER SWAP: current_prev={current_prev}')

            if not main_head:
                main_head = current_next

        logger.debug('-'*40)

        return main_head


def main():
    assert str(Solution().swapPairs(
        head=ListNode(1)
    )) == str(ListNode(1))

    assert str(Solution().swapPairs(
        head=ListNode(1, ListNode(2))
    )) == str(ListNode(2, ListNode(1)))

    assert str(Solution().swapPairs(
        head=ListNode(1, ListNode(2, ListNode(3)))
    )) == str(ListNode(2, ListNode(1, ListNode(3))))

    assert str(Solution().swapPairs(
        head=ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    )) == str(ListNode(2, ListNode(1, ListNode(4, ListNode(3)))))

    assert str(Solution().swapPairs(
        head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    )) == str(ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5))))))

    assert str(Solution().swapPairs(
        head=ListNode(2, ListNode(5, ListNode(3, ListNode(4, ListNode(6, ListNode(2, ListNode(2)))))))
    )) == str(ListNode(5, ListNode(2, ListNode(4, ListNode(3, ListNode(2, ListNode(6, ListNode(2))))))))


if __name__ == '__main__':
    main()
