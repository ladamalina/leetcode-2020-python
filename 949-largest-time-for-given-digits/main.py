import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


import itertools


class Solution:
    def isValid(self, t: List[int]) -> bool:
        if not (0 <= t[0] <= 2):
            return False
        if t[0] == 2:
            if not (0 <= t[1] <= 3):
                return False
        else:
            if not (0 <= t[1] <= 9):
                return False
        if not (0 <= t[2] <= 5):
            return False
        if not (0 <= t[3] <= 9):
            return False

        return True

    def largestTimeFromDigits(self, A: List[int]) -> str:
        logger.debug("-" * 40)
        logger.debug(f"{A=}")
        ts = [
            f"{t[0]}{t[1]}:{t[2]}{t[3]}"
            for t in set(itertools.permutations(A))
            if self.isValid(t)
        ]
        res = max(ts) if ts else ""
        logger.debug(f"{res=}")

        return res


def main():
    assert Solution().largestTimeFromDigits([1,2,3,4]) == "23:41"
    assert Solution().largestTimeFromDigits([5,5,5,5]) == ""
    assert Solution().largestTimeFromDigits([2,0,6,6]) == "06:26"


if __name__ == '__main__':
    main()
