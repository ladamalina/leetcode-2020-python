import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1: List[int] = self.getTreeAsList(root1)
        list2: List[int] = self.getTreeAsList(root2)

        if len(list1) == 0:
            return list2
        if len(list2) == 0:
            return list1

        result: List[int] = []
        i1 = i2 = 0
        while i1 < len(list1) and i2 < len(list2):
            if list1[i1] < list2[i2]:
                result.append(list1[i1])
                i1 += 1
            else:
                result.append(list2[i2])
                i2 += 1
        while i1 < len(list1):
            result.append(list1[i1])
            i1 += 1
        while i2 < len(list2):
            result.append(list2[i2])
            i2 += 1

        return result

    def getTreeAsList(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        return self.getTreeAsList(root.left) + [root.val] + self.getTreeAsList(root.right)


def main():
    pass


if __name__ == '__main__':
    main()
