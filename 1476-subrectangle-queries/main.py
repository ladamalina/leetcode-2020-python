import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self._r: List[List[int]] = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range (row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self._r[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self._r[row][col]


def main():
    pass


if __name__ == '__main__':
    main()
