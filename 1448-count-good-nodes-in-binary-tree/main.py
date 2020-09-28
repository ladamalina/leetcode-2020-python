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
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + self.goodSubnodes(root.left, root.val) + self.goodSubnodes(root.right, root.val)

    def goodSubnodes(self, root: TreeNode, max_path_val: int) -> int:
        if root is None:
            return 0

        num = int(root.val >= max_path_val)
        left_good_subnodes = self.goodSubnodes(root.left, max(root.val, max_path_val))
        right_good_subnodes = self.goodSubnodes(root.right, max(root.val, max_path_val))

        return num + left_good_subnodes + right_good_subnodes


def main():
    pass


if __name__ == '__main__':
    main()
