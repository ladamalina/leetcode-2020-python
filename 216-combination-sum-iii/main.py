import logging
from itertools import combinations
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = list(range(1, n + 1) if n <= 9 else range(1, 10))
        return [comb for comb in combinations(digits, k) if sum(comb) == n]


def main():
    assert Solution().combinationSum3(3, 7) == [[1,2,4]]
    assert Solution().combinationSum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]


if __name__ == '__main__':
    main()
