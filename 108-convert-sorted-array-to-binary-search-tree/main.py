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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) > 1:
            root_i = len(nums) // 2
            return TreeNode(
                val=nums[root_i],
                left=self.sortedArrayToBST(nums[:root_i]),
                right=self.sortedArrayToBST(nums[root_i+1:])
            )
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:  # len(nums) == 0:
            return None


def main():
    bst = Solution().sortedArrayToBST([-10,-3,0,5,9])
    logger.debug(f'bst={bst}')


if __name__ == '__main__':
    main()
