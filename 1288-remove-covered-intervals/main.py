import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        intervals = sorted(intervals)

        i = 0
        while i < len(intervals):
            j = i + 1
            while j < len(intervals):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    intervals = intervals[:j] + intervals[j+1:]
                    continue
                elif intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    intervals = intervals[:i] + intervals[i+1:]
                    i -= 1
                    break
                j += 1
            i += 1

        return len(intervals)


def main():
    assert Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]) == 2
    assert Solution().removeCoveredIntervals([[1,4],[2,3]]) == 1
    assert Solution().removeCoveredIntervals([[0,10],[5,12]]) == 2
    assert Solution().removeCoveredIntervals([[3,10],[4,10],[5,11]]) == 2
    assert Solution().removeCoveredIntervals([[1,2],[1,4],[3,4]]) == 1


if __name__ == '__main__':
    main()
