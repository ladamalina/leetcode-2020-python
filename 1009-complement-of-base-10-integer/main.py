import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n_bin_str = bin(N)[2:]
        c_bin_str = "".join([str(1 - int(_)) for _ in n_bin_str])

        return int(c_bin_str, 2)


def main():
    assert Solution().bitwiseComplement(5) == 2
    assert Solution().bitwiseComplement(7) == 0
    assert Solution().bitwiseComplement(10) == 5


if __name__ == '__main__':
    main()
