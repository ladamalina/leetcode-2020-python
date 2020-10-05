import logging
from collections import defaultdict
from typing import Dict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        logger.debug('-' * 40)
        logger.debug(f'{s1=}, {s2=}')
        if len(s2) < len(s1):
            return False
        diff = self.get_codes_diff(s1, s2)
        d = len(diff.keys())
        logger.debug(f's2_sub={s2[:len(s1)]}, {dict(diff)=}, {d=}')
        if d == 0:
            return True

        i = 1
        while i + len(s1) <= len(s2):
            prev_ch = s2[i - 1]
            diff[prev_ch] -= 1
            if diff[prev_ch] == 0:
                del diff[prev_ch]
                d -= 1
            elif diff[prev_ch] == -1:
                d += 1

            next_ch = s2[i + len(s1) - 1]
            diff[next_ch] += 1
            if diff[next_ch] == 0:
                del diff[next_ch]
                d -= 1
            elif diff[next_ch] == 1:
                d += 1
            logger.debug(f's2_sub={s2[i:i + len(s1)]}, {dict(diff)=}, {d=}')

            if d == 0:
                return True

            i += 1

        return False

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
    assert Solution().checkInclusion("ab", "eidbaooo") is True
    assert Solution().checkInclusion("ab", "eidboaoo") is False
    assert Solution().checkInclusion("hello", "ooolleoooleh") is False


if __name__ == '__main__':
    main()
