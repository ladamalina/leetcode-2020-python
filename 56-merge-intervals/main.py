import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def is_overlapping(self, int1: List[int], int2: List[int]) -> bool:
        return min(int1[1], int2[1]) >= max(int1[0], int2[0])

    def merge_two_ints(self, int1: List[int], int2: List[int]) -> List[int]:
        return [min(int1[0], int2[0]), max(int1[1], int2[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda i: (i[0], i[1]))
        result = []
        for i in range(0, len(intervals)):
            if i == 0:
                result.append(intervals[i])
                continue
            if self.is_overlapping(result[-1], intervals[i]):
                merged = self.merge_two_ints(result[-1], intervals[i])
                result[-1] = merged
            else:
                result.append(intervals[i])

        return result

def main():
    assert Solution().is_overlapping([1,3], [2,6]) is True
    assert Solution().is_overlapping([2,6], [8,10]) is False
    assert Solution().is_overlapping([9,10], [8,11]) is True

    assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert Solution().merge([[1,4],[4,5]]) == [[1,5]]
    assert Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]) == [[1,10]]


if __name__ == '__main__':
    main()
