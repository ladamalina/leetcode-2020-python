import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


def main():
    assert Solution().countOdds(3, 7) == 3
    assert Solution().countOdds(8, 10) == 1


if __name__ == '__main__':
    main()
