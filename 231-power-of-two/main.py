import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        bit_num = n
        while bit_num > 1:
            if bit_num & 1:
                return False
            bit_num >>= 1

        return True

def main():
    assert Solution().isPowerOfTwo(1) is True
    assert Solution().isPowerOfTwo(2) is True
    assert Solution().isPowerOfTwo(8) is True
    assert Solution().isPowerOfTwo(0) is False
    assert Solution().isPowerOfTwo(-1) is False
    assert Solution().isPowerOfTwo(100) is False
    assert Solution().isPowerOfTwo(128) is True


if __name__ == '__main__':
    main()
