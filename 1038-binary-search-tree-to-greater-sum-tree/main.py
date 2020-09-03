import collections
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total_sum = self.sumOfTree(root)
        self.applySum(root, total_sum)

        return root

    def sumOfTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return root.val + self.sumOfTree(root.left) + self.sumOfTree(root.right)

    def applySum(self, root: TreeNode, sum_left: int) -> int:
        if root.left:
            sum_left = self.applySum(root.left, sum_left)

        # no left leaves
        sum_left -= root.val
        root.val = root.val + sum_left

        if root.right:
            sum_left = self.applySum(root.right, sum_left)

        return sum_left

def main():
    pass


if __name__ == '__main__':
    main()
