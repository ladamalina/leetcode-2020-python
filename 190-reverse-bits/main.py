import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def reverseBits(self, n: int) -> int:
        logger.debug('-' * 40)
        logger.debug(f'{n:b}')
        num = n
        power = 31
        result = 0
        while num:
            current = (num & 1) << power
            result += current
            power -= 1
            num = num >> 1
            logger.debug(f'current={current:b}, result={result:b}')

        return result


def main():
    inp = 43261596  # 0x00000010100101000001111010011100
    out = 964176192  # 0x00111001011110000010100101000000
    assert Solution().reverseBits(inp) == out

    inp = 4294967293  # 0x11111111111111111111111111111101
    out = 3221225471  # 0x10111111111111111111111111111111
    assert Solution().reverseBits(inp) == out


if __name__ == '__main__':
    main()
