import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
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
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    logger.debug('-' * 40)
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    logger.debug('-' * 40)
    assert Solution().plusOne([4, 3, 2, 9]) == [4, 3, 3, 0]
    logger.debug('-' * 40)
    assert Solution().plusOne([9]) == [1, 0]
    logger.debug('-' * 40)
    assert Solution().plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0]


if __name__ == '__main__':
    main()
