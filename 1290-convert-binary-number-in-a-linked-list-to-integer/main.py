import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_as_str = str(head.val)
        while head.next:
            bin_as_str += str(head.next.val)
            head = head.next

        return int(bin_as_str, 2)


def main():
    pass


if __name__ == '__main__':
    main()
