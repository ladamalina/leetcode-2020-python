import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars: Dict[str, int] = dict()
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
        evens: List[int] = []
        odds: List[int] = []
        max_odd = 0
        for ch in chars:
            if chars[ch] % 2 == 0:
                evens.append(chars[ch])
            else:
                if chars[ch] > max_odd:
                    max_odd = chars[ch]
                odds.append(chars[ch])
        if max_odd in odds:
            odds.remove(max_odd)
        result = sum(evens) + max_odd + sum([_ - 1 for _ in odds])

        return result


def main():
    assert Solution().longestPalindrome("abccccdd") == 7
    assert Solution().longestPalindrome("bb") == 2


if __name__ == '__main__':
    main()
