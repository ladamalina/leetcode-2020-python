import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()

        remove_count = 0
        current_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < current_end:  # overlap
                remove_count += 1
                current_end = min(current_end, intervals[i][1])
            else:
                current_end = intervals[i][1]

        return remove_count


def main():
    assert Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    assert Solution().eraseOverlapIntervals([[1,2],[2,3]]) == 0
    assert Solution().eraseOverlapIntervals([[1,2]]) == 0


if __name__ == '__main__':
    main()
