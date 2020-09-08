import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        """
        Do not return anything, modify matrix in-place instead.
        """
        reset_first_row = False
        reset_first_col = False
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[0][col] = None
                    matrix[row][0] = None
                    if row == 0:
                        reset_first_row = True
                    if col == 0:
                        reset_first_col = True

        for row in range(1, len(matrix)):
            if matrix[row][0] is None:
                matrix[row] = [0] * len(matrix[row])

        for col in range(1, len(matrix[0])):
            if matrix[0][col] is None:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        if reset_first_row:
            matrix[0] = [0] * len(matrix[row])

        if reset_first_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0


def main():
    input = [[1,1,1],[0,1,2]]
    Solution().setZeroes(input)
    assert input == [[0,1,1],[0,0,0]]

    input = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(input)
    assert input == [[1,0,1],[0,0,0],[1,0,1]]

    input = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(input)
    assert input == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    input = [[-1],[2],[3]]
    Solution().setZeroes(input)
    assert input == [[-1],[2],[3]]


if __name__ == '__main__':
    main()
