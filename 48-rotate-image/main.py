import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        mlen = len(matrix[0])
        layers_num = mlen//2
        # iterate layers
        for l in range(layers_num):
            # rotate cells
            first_cell = l
            last_cell = mlen - 2 - l
            for c in range(first_cell, last_cell+1):
                tmp = matrix[l][c]
                matrix[l][c] = matrix[mlen - 1 - c][l]
                matrix[mlen - 1 - c][l] = matrix[mlen - 1 - l][mlen - 1 - c]
                matrix[mlen - 1 - l][mlen - 1 - c] = matrix[c][mlen - 1 - l]
                matrix[c][mlen - 1 - l] = tmp


def main():
    matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    Solution().rotate(matrix)
    assert matrix == [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]


if __name__ == '__main__':
    main()
