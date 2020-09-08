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
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isSymmetricBrances(root.left, root.right)

    def isSymmetricBrances(self, rootLeft: TreeNode, rootRight: TreeNode) -> bool:
        if rootLeft is None and rootRight is None:
            return True

        if rootLeft is None and rootRight is not None:
            return False

        if rootLeft is not None and rootRight is None:
            return False

        # rootLeft is not None and rootRight is not None
        if rootLeft.val != rootRight.val:
            return False
        # rootLeft.val == rootRight.val

        return self.isSymmetricBrances(rootLeft.left, rootRight.right) and \
            self.isSymmetricBrances(rootLeft.right, rootRight.left)


def main():
    assert Solution().isSymmetric(
        TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                 right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    ) is True

    assert Solution().isSymmetric(
        TreeNode(1, left=TreeNode(2, right=TreeNode(3)),
                 right=TreeNode(2, right=TreeNode(3)))
    ) is False


if __name__ == '__main__':
    main()
