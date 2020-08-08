import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def pathSum(self, root: TreeNode, s: int):
        return self.countTargetsSum(root, s, [s])

    def countTargetsSum(self, node: TreeNode, origin_sum: int, targets: List[int]):
        if not node:
            return 0
        hit = 0
        for t in targets:
            if not t - node.val:
                hit += 1
        targets = [t - node.val for t in targets] + [origin_sum]
        return hit + self.countTargetsSum(node.left, origin_sum, targets) + self.countTargetsSum(node.right, origin_sum, targets)

def main():
    pass


if __name__ == '__main__':
    main()
