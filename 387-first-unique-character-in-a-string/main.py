import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = dict()
        for i, ch in enumerate(s):
            if ch in seen:
                seen[ch]["count"] += 1
            else:
                seen[ch] = {"first_i": i, "count": 1}

        seen_earlier_i = None
        for ch in seen:
            if seen[ch]["count"] > 1:
                continue
            if seen_earlier_i is None or seen[ch]["first_i"] < seen_earlier_i:
                seen_earlier_i = seen[ch]["first_i"]

        return seen_earlier_i if seen_earlier_i is not None else -1


def main():
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    assert Solution().firstUniqChar("") == -1
    assert Solution().firstUniqChar("abcd") == 0
    assert Solution().firstUniqChar("aaa") == -1
    assert Solution().firstUniqChar("a") == 0


if __name__ == '__main__':
    main()
