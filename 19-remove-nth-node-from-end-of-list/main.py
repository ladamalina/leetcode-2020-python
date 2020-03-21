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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # logging.warning(f'head={head}, n={n}')
        nodes = dict()
        current_node = head
        total_nodes = 1
        while True:
            nodes[total_nodes] = current_node
            if current_node.next:
                next_node = current_node.next
                del current_node
                current_node = next_node
                total_nodes += 1
            else:
                break

        # logging.warning(f'total_nodes={total_nodes}')
        if n == total_nodes == 1:
            return None
        elif n == total_nodes:
            # remove head
            return nodes[2]
        elif n == 1:
            nodes[total_nodes - 1].next = None
            return head
        else:
            nodes[total_nodes - n].next = nodes[total_nodes - n + 2]
            return head


def main():
    assert str(Solution().removeNthFromEnd(
        head=ListNode(2, ListNode(4, ListNode(3))), n=2)) == str(ListNode(2, ListNode(3)))
    assert str(Solution().removeNthFromEnd(
        head=ListNode(2, ListNode(4, ListNode(3))), n=1)) == str(ListNode(2, ListNode(4)))
    assert str(Solution().removeNthFromEnd(
        head=ListNode(2, ListNode(4, ListNode(3))), n=3)) == str(ListNode(4, ListNode(3)))
    assert str(Solution().removeNthFromEnd(
        head=ListNode(2, ListNode(4)), n=1)) == str(ListNode(2))
    assert str(Solution().removeNthFromEnd(
        head=ListNode(2, ListNode(4)), n=2)) == str(ListNode(4))
    assert str(Solution().removeNthFromEnd(
        head=ListNode(1), n=1)) == str(None)


if __name__ == '__main__':
    main()
