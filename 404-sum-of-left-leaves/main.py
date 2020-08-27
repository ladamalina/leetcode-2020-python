import logging
from queue import Queue

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def sumOfLeftOfLeft(self, node: TreeNode) -> int:
        if node.left is None and node.right is None:
            return node.val

        sum_of_left = self.sumOfLeftOfLeft(node.left) if node.left else 0
        sum_of_right = self.sumOfLeftOfRight(node.right) if node.right else 0

        return sum_of_left + sum_of_right

    def sumOfLeftOfRight(self, node: TreeNode) -> int:
        if node.left is None and node.right is None:
            return 0

        sum_of_left = self.sumOfLeftOfLeft(node.left) if node.left else 0
        sum_of_right = self.sumOfLeftOfRight(node.right) if node.right else 0

        return sum_of_left + sum_of_right

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.sumOfLeftOfRight(root)


def main():
    assert Solution().sumOfLeftLeaves(TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))) == 24
    assert Solution().sumOfLeftLeaves(TreeNode(3)) == 0
    assert Solution().sumOfLeftLeaves(TreeNode(3, left=None, right=TreeNode(5))) == 0


if __name__ == '__main__':
    main()
