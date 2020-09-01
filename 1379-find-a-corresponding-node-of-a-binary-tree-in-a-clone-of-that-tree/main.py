import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        original_path = self.get_path_to_target(original, target)
        if original_path is True:
            return cloned

        # type(original_path) is list
        current_node = cloned
        for step in original_path:
            if step == 0:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return current_node

    def get_path_to_target(self, root: TreeNode, target: TreeNode):
        if not root:
            return False

        if root is target:
            return True

        path_on_left = self.get_path_to_target(root.left, target)
        if path_on_left is True:
            return [0]
        elif type(path_on_left) is list:
            return [0] + path_on_left

        path_on_right = self.get_path_to_target(root.right, target)
        if path_on_right is True:
            return [1]
        elif type(path_on_right) is list:
            return [1] + path_on_right

        return False


def main():
    pass


if __name__ == '__main__':
    main()
