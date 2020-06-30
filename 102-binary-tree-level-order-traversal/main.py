import json
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        l = []
        def append_level(root: TreeNode, level: int, l: List[List[int]]):
            if root is None:
                return
            if len(l) > level:
                l[level].append(root.val)
            else:
                l.append([root.val])
            append_level(root.left, level+1, l)
            append_level(root.right, level+1, l)

        append_level(root, 0, l)
        return l


def main():
    # [3,9,20,null,null,15,7]
    expexted = [[3], [9, 20], [15, 7]]
    actual = Solution().levelOrder(
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    )
    logger.debug(f'expexted={expexted}, actual={actual}')
    assert expexted == actual


if __name__ == '__main__':
    main()
