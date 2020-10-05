import logging
from collections import defaultdict
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        idx: List[int] = []
        diff = self.get_codes_diff(p, s)
        d = len(diff.keys())
        if d == 0:
            idx.append(0)

        i = 1
        while i + len(p) <= len(s):
            prev_ch = s[i - 1]
            diff[prev_ch] -= 1
            if diff[prev_ch] == 0:
                del diff[prev_ch]
                d -= 1
            elif diff[prev_ch] == -1:
                d += 1

            next_ch = s[i + len(p) - 1]
            diff[next_ch] += 1
            if diff[next_ch] == 0:
                del diff[next_ch]
                d -= 1
            elif diff[next_ch] == 1:
                d += 1

            if d == 0:
                idx.append(i)

            i += 1

        return idx

    def get_str_code(self, s: str) -> Dict[str, int]:
        code: Dict[str, int] = defaultdict(lambda: 0)
        for ch in s:
            code[ch] += 1

        return dict(code)

    def get_codes_diff(self, s1: str, s2: str) -> Dict[str, int]:
        c1: Dict[str, int] = self.get_str_code(s1)
        c2: Dict[str, int] = self.get_str_code(s2[:len(s1)])

        diff: Dict[str, int] = defaultdict(lambda: 0)
        union_chars = set(list(c1.keys()) + list(c2.keys()))
        for ch in union_chars:
            if c1.get(ch, 0) != c2.get(ch, 0):
                diff[ch] = c2.get(ch, 0) - c1.get(ch, 0)

        return diff


def main():
    assert Solution().findAnagrams(s="cbaebabacd", p="abc") == [0, 6]
    assert Solution().findAnagrams(s="abab", p="ab") == [0, 1, 2]


if __name__ == '__main__':
    main()
