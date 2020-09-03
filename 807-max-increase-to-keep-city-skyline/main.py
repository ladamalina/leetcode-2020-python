import logging
import re
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0

        left_view = []
        for row_i in range(len(grid)):
            left_view.append(max(grid[row_i]))

        top_view = []
        for col_i in range(len(grid[0])):
            top_view.append(max([_[col_i] for _ in grid]))

        max_inc = 0
        for row_i in range(len(grid)):
            for col_i in range(len(grid[0])):
                skyline = min(left_view[row_i], top_view[col_i])
                if grid[row_i][col_i] < skyline:
                    max_inc += skyline - grid[row_i][col_i]

        return max_inc


def main():
    assert Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]) == 35


if __name__ == '__main__':
    main()
