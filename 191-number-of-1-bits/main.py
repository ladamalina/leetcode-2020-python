import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        for i in range(0, 32):
            if mask & n != 0:
                bits += 1
            mask <<= 1

        return bits


def main():
    assert Solution().hammingWeight(0x00000000000000000000000000001011) == 3
    assert Solution().hammingWeight(0x00000000000000000000000010000000) == 1
    assert Solution().hammingWeight(4294967293) == 31  # 0x11111111111111111111111111111101


if __name__ == '__main__':
    main()
