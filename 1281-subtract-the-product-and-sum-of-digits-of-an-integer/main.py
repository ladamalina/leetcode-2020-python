import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(_) for _ in list(str(n))]
        n_product = 1
        n_sum = 0
        for d in digits:
            n_product *= d
            n_sum += d

        return n_product - n_sum


def main():
    assert Solution().subtractProductAndSum(234) == 15


if __name__ == '__main__':
    main()
