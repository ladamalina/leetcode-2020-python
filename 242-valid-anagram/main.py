import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = dict()
        seen_t = dict()

        for i in range(0, len(s)):
            if s[i] in seen_s:
                seen_s[s[i]] += 1
            else:
                seen_s[s[i]] = 1
            if t[i] in seen_t:
                seen_t[t[i]] += 1
            else:
                seen_t[t[i]] = 1

        s_keys = list(seen_s.keys())
        for s_key in s_keys:
            if seen_s[s_key] != seen_t.get(s_key):
                return False
            else:
                del seen_s[s_key]
                del seen_t[s_key]

        if len(seen_t.keys()):
            return False

        return True


def main():
    assert Solution().isAnagram("anagram", "nagaram") == True
    assert Solution().isAnagram("rat", "car") == False
    assert Solution().isAnagram("rat", "cart") == False
    assert Solution().isAnagram("", "") == True
    assert Solution().isAnagram("", "non") == False


if __name__ == '__main__':
    main()
