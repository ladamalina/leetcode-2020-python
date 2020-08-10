import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def titleToNumber(self, s: str) -> int:
        alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d: Dict[str, int] = {ch: i + 1 for i, ch in enumerate(alphas)}

        num = 0
        for i in range(len(s)):
            ch = s[-1 * (i + 1)]
            num += len(alphas) ** i * d[ch]

        return num


def main():
    assert Solution().titleToNumber("A") == 1
    assert Solution().titleToNumber("AB") == 28
    assert Solution().titleToNumber("ZZ") == 702
    assert Solution().titleToNumber("AAA") == 703
    assert Solution().titleToNumber("BBB") == 1406


if __name__ == '__main__':
    main()
