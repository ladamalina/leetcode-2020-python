import logging


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        next_str = f' -> {self.next.__repr__()}' if self.next else ''
        return f'{self.val}{next_str}'


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_node = last_node = None

        cur_l1 = l1
        cur_l2 = l2
        overflow = 0

        while cur_l1 or cur_l2:
            cur_l1_val = cur_l1.val if cur_l1 else 0
            cur_l2_val = cur_l2.val if cur_l2 else 0
            sum_cur = cur_l1_val + cur_l2_val + overflow
            # logging.warning(f'cur_l1_val={cur_l1_val}, cur_l2_val={cur_l2_val}, overflow={overflow}, sum_cur={sum_cur}')

            cur_val = sum_cur % 10
            overflow = sum_cur // 10

            current_node = ListNode(cur_val)
            if last_node:
                last_node.next = current_node
                del last_node
            last_node = current_node
            if not first_node:
                first_node = last_node

            cur_l1 = cur_l1.next if cur_l1 else None
            cur_l2 = cur_l2.next if cur_l2 else None

        if overflow:
            last_node.next = ListNode(overflow)
        # logging.warning(f'first_node={first_node}')

        return first_node


def main():
    assert str(Solution().addTwoNumbers(
        l1=ListNode(2, ListNode(4, ListNode(3))),
        l2=ListNode(5, ListNode(6, ListNode(4)))
    )) == str(ListNode(7, ListNode(0, ListNode(8))))

    assert str(Solution().addTwoNumbers(
        l1=ListNode(5),
        l2=ListNode(5)
    )) == str(ListNode(0, ListNode(1)))

    assert str(Solution().addTwoNumbers(
        l1=ListNode(2),
        l2=ListNode(9, ListNode(6))
    )) == str(ListNode(1, ListNode(7)))


if __name__ == '__main__':
    main()
