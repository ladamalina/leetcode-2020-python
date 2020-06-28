import logging
import re
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # logger.debug('-'*40)
        # logger.debug(f'nums1={nums1}, m={m}, nums2={nums2}, n={n}')
        if n == 0:
            return

        for i in range(m+n-1, m-1, -1):
            nums1.pop(i)
        # logger.debug(f'after pop: nums1={nums1}')

        i1 = 0
        i2 = 0
        while i1 < len(nums1) or i2 < n:
            # logger.debug(f'before: i1={i1}, i2={i2}, nums1={nums1}, nums2={nums2}')
            if i1 >= len(nums1):
                nums1.insert(i1, nums2[i2])
                i1 += 1
                i2 += 1
                continue
            if i2 >= n:
                i1 += 1
                continue

            if nums1[i1] <= nums2[i2]:
                i1 += 1
            else:
                nums1.insert(i1, nums2[i2])
                i1 += 1
                i2 += 1


        # logger.debug(f'finally nums1={nums1}')


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = []
    Solution().merge(nums1, 0, [], 0)
    assert nums1 == []

    nums1 = [0, 0, 0]
    Solution().merge(nums1, 0, [1, 1, 1], 3)
    assert nums1 == [1, 1, 1]

    nums1 = [3, 0, 0]
    Solution().merge(nums1, 1, [1, 2], 2)
    assert nums1 == [1, 2, 3]


if __name__ == '__main__':
    main()
