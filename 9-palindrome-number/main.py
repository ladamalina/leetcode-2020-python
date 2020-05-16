import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        digits_num = int(math.log10(x)) + 1
        half_of_digits = digits_num // 2
        odd_digits = bool(digits_num % 2)

        tmp_x = x
        reversed_x = 0
        tmp_x_len = digits_num
        len_to_proceed = half_of_digits+1 if odd_digits else half_of_digits
        while tmp_x_len > len_to_proceed:
            digit = tmp_x % 10
            reversed_x = reversed_x*10 + digit
            tmp_x = tmp_x // 10
            tmp_x_len -= 1

        if odd_digits:
            return tmp_x // 10 == reversed_x
        else:
            return tmp_x == reversed_x


def main():
    assert Solution().isPalindrome(0) == True
    assert Solution().isPalindrome(1) == True
    assert Solution().isPalindrome(-1) == False
    assert Solution().isPalindrome(-12) == False
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(12) == False
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(112211) == True
    assert Solution().isPalindrome(1123211) == True


if __name__ == '__main__':
    main()
