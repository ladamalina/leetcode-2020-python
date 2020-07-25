import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        logging.debug(f"{A=}")
        negatives = []
        squares = []
        for i, num in enumerate(A):
            logging.debug(f"{num=}, {negatives=}, {squares=}")
            if num < 0:
                negatives.append(num ** 2)
                continue

            # num >= 0
            num_sq = num ** 2
            num_sq_appended = False
            if len(negatives):
                for j in range(len(negatives) - 1, -1, -1):
                    if num_sq <= negatives[j]:
                        squares.append(num_sq)
                        num_sq_appended = True
                        break
                    # num_sq > negatives[j]
                    squares.append(negatives[j])
                    negatives.pop(j)
                if num_sq_appended:
                    continue

            # len(negatives) == 0
            squares.append(num_sq)

        if len(negatives):
            for j in range(len(negatives) - 1, -1, -1):
                squares.append(negatives[j])

        return squares


def main():
    expected = [0,1,9,16,100]
    actual = Solution().sortedSquares([-4,-1,0,3,10])
    logger.debug(f"{expected=}, {actual=}")
    assert actual == expected
    assert Solution().sortedSquares([-4,-3,-2,-1]) == [1,4,9,16]
    assert Solution().sortedSquares([0,1,2,3]) == [0,1,4,9]
    assert Solution().sortedSquares([-1,-1,-1,-1,-1]) == [1,1,1,1,1]


if __name__ == '__main__':
    main()
