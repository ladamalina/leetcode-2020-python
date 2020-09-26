import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def maximum69Number(self, num: int) -> int:
        s = list(str(num))
        for i, ch in enumerate(s):
            if ch == '6':
                s[i] = '9'
                break

        return int(''.join(s))


def main():
    assert Solution().maximum69Number(9669) == 9969
    assert Solution().maximum69Number(9996) == 9999
    assert Solution().maximum69Number(9999) == 9999


if __name__ == '__main__':
    main()
