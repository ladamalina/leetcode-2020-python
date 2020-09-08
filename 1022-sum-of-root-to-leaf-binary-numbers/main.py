import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        leaf_bins: List[str] = self.getLeafBins(root)
        leaf_ints: List[int] = [int(_, 2) for _ in leaf_bins]

        return sum(leaf_ints) if leaf_ints else 0

    def getLeafBins(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        result: List[str] = []

        left_bins: List[str] = self.getLeafBins(root.left)
        left_result: List[str] = [str(root.val) + _ for _ in left_bins]

        right_bins: List[str] = self.getLeafBins(root.right)
        right_result: List[str] = [str(root.val) + _ for _ in right_bins]

        if left_result or right_result:
            return left_result + right_result

        return [str(root.val)]


def main():
    pass


if __name__ == '__main__':
    main()
