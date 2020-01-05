class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        is_positive = x > 0
        tmp_x = abs(x)
        reversed_x = 0

        while tmp_x > 0:


def main():
    assert Solution().reverse(0) == 0
    assert Solution().reverse(1) == 1
    assert Solution().reverse(-1) == -1
    assert Solution().reverse(-12) == -21
    assert Solution().reverse(-121) == -121
    assert Solution().reverse(12) == 21
    assert Solution().reverse(120) == 21
    assert Solution().reverse(121) == 121
    assert Solution().reverse(123) == 321
    assert Solution().reverse(11234) == 43211
    assert Solution().reverse(112340) == 43211
    assert Solution().reverse(11223344) == 44332211


if __name__ == '__main__':
    main()
