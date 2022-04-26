import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return self.hammingWeight(x ^ y)

    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(0, 32):
            if mask & n != 0:
                bits += 1
            mask <<= 1

        return bits


def main():
    assert Solution().hammingDistance(1, 4) == 2


if __name__ == '__main__':
    main()
