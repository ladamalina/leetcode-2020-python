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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        logger.debug('-' * 40)
        if root is None or root.left is None or root.right is None:
            return False
        if root.val == x or root.val == y:
            return False

        x_found_at_level = None
        x_parent = None
        y_found_at_level = None
        y_parent = None
        q = Queue()
        q.put((root.left, 1, root.val))
        q.put((root.right, 1, root.val))
        current_level = 1
        while not q.empty():
            node = q.get()
            logger.debug(f'node={node[0]}, level={node[1]}, parent={node[2]}, x_found_at_level={x_found_at_level}, y_found_at_level={y_found_at_level}')
            if node[1] > current_level:
                current_level = node[1]
                if (x_found_at_level is not None and y_found_at_level is None) or (x_found_at_level is None and y_found_at_level is not None):
                    return False

            if node[0].val == x:
                x_found_at_level = current_level
                x_parent = node[2]
            if node[0].val == y:
                y_found_at_level = current_level
                y_parent = node[2]
            if x_found_at_level is not None and x_found_at_level == y_found_at_level and x_parent != y_parent:
                return True

            if node[0].left is not None:
                q.put((node[0].left, current_level + 1, node[0].val))
            if node[0].right is not None:
                q.put((node[0].right, current_level + 1, node[0].val))

        return False


def main():
    assert Solution().isCousins(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), x=4, y=3) is False
    assert Solution().isCousins(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), x=5, y=4) is True
    assert Solution().isCousins(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), x=2, y=3) is False


if __name__ == '__main__':
    main()
