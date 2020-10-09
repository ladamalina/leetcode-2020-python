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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        root_is_target_leaf = self.removeLeaf(root, target)
        if root_is_target_leaf:
            del root
            return None

        return root

    def removeLeaf(self, root: TreeNode, target: int) -> bool:
        if root is None:
            return False
        at_left = self.removeLeaf(root.left, target)
        if at_left:
            root.left = None
        at_right = self.removeLeaf(root.right, target)
        if at_right:
            root.right = None
        if root.val == target and root.left is None and root.right is None:
            return True
        return False


def main():
    pass


if __name__ == '__main__':
    main()
