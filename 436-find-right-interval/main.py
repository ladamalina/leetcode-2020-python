import bisect
import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([I[0], i] for i, I in enumerate(intervals)) + [[float('inf'), -1]]
        return [starts[bisect.bisect(starts, [I[1]])][1] for I in intervals]


def main():
    assert Solution().findRightInterval([ [1,2] ]) == -1
    assert Solution().findRightInterval([ [3,4], [2,3], [1,2] ]) == [-1, 0, 1]
    assert Solution().findRightInterval([ [1,4], [2,3], [3,4] ]) == [-1, 2, -1]


if __name__ == '__main__':
    main()
