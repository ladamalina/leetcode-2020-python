import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2:  # odd
                num -= 1
            else:  # even
                num /= 2
            steps += 1

        return steps


def main():
    assert Solution().numberOfSteps(14) == 6


if __name__ == '__main__':
    main()
