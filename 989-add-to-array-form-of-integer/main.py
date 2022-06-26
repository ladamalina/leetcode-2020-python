import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        logger.debug(f'{A=}, {K=}')
        k_big = K // 10
        k_small = K % 10

        # len(A) > 0, K > 0
        if len(A) > 0 and K > 0:
            last_sum = A[-1] + k_small
            if last_sum < 10:
                return self.addToArrayForm(A[:-1], k_big) + [last_sum]
            else:
                return self.addToArrayForm(A[:-1], k_big + 1) + [last_sum - 10]

        # len(A) > 0, K == 0
        if len(A) > 0 and K == 0:
            return A

        # len(A) == 0, K > 0
        if len(A) == 0 and K > 0:
            return self.addToArrayForm([], k_big) + [k_small]

        # len(A) == 0, K == 0
        if len(A) == 0 and K == 0:
            return []


    def plusOne(self, digits: List[int]) -> List[int]:
        logger.debug(f'{digits}')
        last_sum = digits[-1] + 1
        if last_sum < 10:
            digits[-1] = last_sum
            return digits
        if len(digits) == 1:
            return [1, last_sum - 10]

        return self.plusOne(digits[:-1]) + [last_sum - 10]


def main():
    logger.debug('-' * 40)
    assert Solution().addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]
    logger.debug('-' * 40)
    assert Solution().addToArrayForm([2, 7, 4], 181) == [4, 5, 5]
    logger.debug('-' * 40)
    assert Solution().addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
    logger.debug('-' * 40)
    assert Solution().addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


if __name__ == '__main__':
    main()
