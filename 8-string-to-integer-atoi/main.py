import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def myAtoi(self, str: str) -> int:
        sign_is_found = False
        is_positive = True
        first_digit_is_found = False
        num = 0
        signs = {'-', '+'}

        for ch in str:
            if ch == ' ':
                if sign_is_found or first_digit_is_found:
                    break
                continue
            if ch in signs:
                if sign_is_found or first_digit_is_found:
                    break
                if ch == '+':
                    sign_is_found = True
                    continue
                if ch == '-':
                    sign_is_found = True
                    is_positive = False
                    continue
            if ch.isdigit():
                first_digit_is_found = True
                num = num * 10 + int(ch)
            else:
                break

        num = num if is_positive else num * -1
        if (-0x7fffffff) <= num <= (0x7fffffff-1):
            pass
        elif num > 0:
            num = 0x7fffffff
        else:
            num = -0x7fffffff - 1

        return num


def main():
    assert Solution().myAtoi("42") == 42
    assert Solution().myAtoi("  -42") == -42
    assert Solution().myAtoi("4193 with words") == 4193
    assert Solution().myAtoi("words and 987") == 0
    assert Solution().myAtoi("-91283472332") == -2147483648


if __name__ == '__main__':
    main()
