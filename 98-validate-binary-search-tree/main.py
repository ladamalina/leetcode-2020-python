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
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isValidBSSubtree(root.left, high_n=root.val) \
            and self.isValidBSSubtree(root.right, low_n=root.val)

    def isValidBSSubtree(self, root: TreeNode, low_n: int = None, high_n: int = None) -> bool:
        if root is None:
            return True

        if low_n is None and high_n is not None:
            if root.val >= high_n:
                return False
            return self.isValidBSSubtree(root.left, high_n=root.val) \
                and self.isValidBSSubtree(root.right, low_n=root.val, high_n=high_n)

        if low_n is not None and high_n is None:
            if root.val <= low_n:
                return False
            return self.isValidBSSubtree(root.left, low_n=low_n, high_n=root.val) \
                and self.isValidBSSubtree(root.right, low_n=root.val)

        if low_n is not None and high_n is not None:
            if root.val <= low_n or root.val >= high_n:
                return False
            return self.isValidBSSubtree(root.left, low_n=low_n, high_n=root.val) \
                and self.isValidBSSubtree(root.right, low_n=root.val, high_n=high_n)


def main():
    assert Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))) == True
    assert Solution().isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))) == False
    assert Solution().isValidBST(TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))) == False


if __name__ == '__main__':
    main()
