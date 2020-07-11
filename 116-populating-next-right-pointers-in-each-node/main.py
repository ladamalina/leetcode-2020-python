import logging
from queue import Queue

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def walk_sym(self, root: Node, level: int) -> None:
        if root is None:
            return

        if level in self.memo:
            self.memo[level].next = root
        self.memo[level] = root

        self.walk_sym(root.left, level=level + 1)
        self.walk_sym(root.right, level=level + 1)

    def connect(self, root: Node) -> Node:
        self.memo: Dict[int, Node] = dict()  # max keys number is 12
        self.walk_sym(root, level=0)

        return root


def main():
    pass


if __name__ == '__main__':
    main()
