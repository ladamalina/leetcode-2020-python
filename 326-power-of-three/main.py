import logging
import math
import sys
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_int = sys.maxsize
        max_power = math.floor(math.log(max_int, 3))
        max_powered = 3 ** max_power

        return n > 0 and max_powered % n == 0


def main():
    assert Solution().isPowerOfThree(27) is True
    assert Solution().isPowerOfThree(0) is False
    assert Solution().isPowerOfThree(9) is True
    assert Solution().isPowerOfThree(45) is False


if __name__ == '__main__':
    main()
