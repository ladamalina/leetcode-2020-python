from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums_a = nums1
            nums_b = nums2
        else:
            nums_a = nums2
            nums_b = nums1

        median = None
        min_index = 0
        max_index = len(nums_a)
        while min_index <= max_index:
            i = (min_index + max_index) // 2
            j = (len(nums_a) + len(nums_b) + 1) // 2 - i
            if i < len(nums_a) and j > 0 and nums_b[j - 1] > nums_a[i]:
                min_index = i + 1
            elif i > 0 and j < len(nums_b) and nums_b[j] < nums_a[i - 1]:
                max_index = i - 1
            else:
                if i == 0:
                    median = nums_b[j - 1]
                elif j == 0:
                    median = nums_a[i - 1]
                else :
                    median = max(nums_a[i - 1], nums_b[j - 1])
                break

        if (len(nums_a) + len(nums_b)) % 2 == 1:
            return median

        if i == len(nums_a):
            return (median + nums_b[j]) / 2

        if j == len(nums_b):
            return (median + nums_a[i]) / 2

        return (median + min(nums_a[i], nums_b[j])) / 2


def main():
    assert Solution().findMedianSortedArrays([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]) == 3
    assert Solution().findMedianSortedArrays([2, 3, 5, 8], [10, 12, 14, 16, 18, 20]) == 11
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5


if __name__ == '__main__':
    main()
