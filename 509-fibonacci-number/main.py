import logging
from typing import Dict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

mem: Dict[int, int] = dict()


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        elif N == 2:
            return 1
        else:
            if N not in mem:
                mem[N] = self.fib(N - 1) + self.fib(N - 2)
            return mem[N]


def main():
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3


if __name__ == '__main__':
    main()
