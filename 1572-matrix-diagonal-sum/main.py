import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i]
            j = len(mat) - 1 - i
            if j != i:
                s += mat[i][j]

        return s


def main():
    assert Solution().diagonalSum([[1,2,3],[4,5,6],[7,8,9]]) == 25
    assert Solution().diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 8
    assert Solution().diagonalSum([[5]]) == 5
    assert Solution().diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]) == 55


if __name__ == '__main__':
    main()
