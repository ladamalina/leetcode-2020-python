import logging
from math import ceil, log
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return False if num <= 0 else 4 ** ceil(log(num, 4)) == num


def main():
    assert Solution().isPowerOfFour(16) is True
    assert Solution().isPowerOfFour(1) is True
    assert Solution().isPowerOfFour(2) is False
    assert Solution().isPowerOfFour(0) is False


if __name__ == '__main__':
    main()
