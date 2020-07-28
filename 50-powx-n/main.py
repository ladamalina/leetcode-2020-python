import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def pow(self, x: float, n: int) -> float:
        logger.debug(f'pow: {x=}, {n=}')
        if n == 0:
            return 1
        if n == 1:
            return x

        if n % 2:
            return x * self.pow(x, n - 1)
        else:
            half_pow = self.pow(x, n // 2)
            return half_pow * half_pow

    def myPow(self, x: float, n: int) -> float:
        logger.debug('-' * 40)
        logger.debug(f'{x=}, {n=}')
        if x == 0:
            logger.debug(f'num={x}')
            return x
        if n == 0:
            logger.debug(f'num={1.0}')
            return 1.0
        if n == 1:
            logger.debug(f'num={x}')
            return x
        if n == -1:
            logger.debug(f'num={1/x}')
            return 1/x

        pow = n if n > 0 else n * -1
        num = self.pow(x, pow)
        if n < 0:
            num = 1/num

        logger.debug(f'{num=}')
        return num


def main():
    assert Solution().myPow(2., 10) == 1024.
    assert Solution().myPow(.0, 2) == .0
    assert Solution().myPow(2., 0) == 1.
    assert Solution().myPow(2., 1) == 2.
    assert Solution().myPow(0.00001, 2147483647) == 1024.


if __name__ == '__main__':
    main()
