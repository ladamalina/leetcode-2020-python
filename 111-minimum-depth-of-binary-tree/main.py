import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is not None:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        elif root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1


def main():
    # [3,9,20,null,null,15,7]
    assert Solution().minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))) == 2
    # [1,2]
    assert Solution().minDepth(TreeNode(1, TreeNode(2))) == 2
    # []
    assert Solution().minDepth(None) == 0


if __name__ == '__main__':
    main()
