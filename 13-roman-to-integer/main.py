import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

digits = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
spec_pairs = {
    ("I", "V"), ("I", "X"),
    ("X", "L"), ("X", "C"),
    ("C", "D"), ("C", "M"),
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            current_value = digits.get(s[i])
            if i == len(s) - 1:
                result += current_value
                break
            next_value = digits.get(s[i+1])
            if current_value < next_value and (s[i], s[i+1]) in spec_pairs:
                result += next_value - current_value
                i += 2
            elif current_value >= next_value:
                result += current_value
                i += 1
            else:
                break

        return result


def main():
    assert Solution().romanToInt("") == 0
    assert Solution().romanToInt("I") == 1
    assert Solution().romanToInt("D") == 500
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994


if __name__ == '__main__':
    main()
