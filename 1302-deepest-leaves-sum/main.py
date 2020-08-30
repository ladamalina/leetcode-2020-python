import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._depths: Dict[int, List[int]] = dict()

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.fillDepths(root, 0)
        max_depth = max(self._depths.keys())

        return sum(self._depths[max_depth])

    def fillDepths(self, root: TreeNode, depth: int) -> None:
        if not root:
            return

        if depth in self._depths:
            self._depths[depth].append(root.val)
        else:
            self._depths[depth] = [root.val]

        self.fillDepths(root.left, depth + 1)
        self.fillDepths(root.right, depth + 1)


def main():
    pass


if __name__ == '__main__':
    main()
