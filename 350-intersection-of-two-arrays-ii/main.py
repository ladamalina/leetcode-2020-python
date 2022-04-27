import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
                continue
            if nums1[i1] < nums2[i2]:
                i1 += 1
                continue
            if nums1[i1] > nums2[i2]:
                i2 += 1
                continue

        return result


def main():
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert Solution().intersect([], [9, 4, 9, 8, 4]) == []
    assert Solution().intersect([], []) == []


if __name__ == '__main__':
    main()
