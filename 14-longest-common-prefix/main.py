import logging
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str, min_str_i = self.get_min_item(strs)
        possible_pref = min_str
        if possible_pref == "":
            return possible_pref
        for i, el in enumerate(strs):
            if i == min_str_i:
                continue
            while not el.startswith(possible_pref):
                possible_pref = possible_pref[:-1]
                if possible_pref == "":
                    return possible_pref

        return possible_pref


    def get_min_item(self, strs: List[str]) -> Tuple[str, int]:
        if not strs:
            return "", None
        min_str = strs[0]
        min_str_i = 0
        for i, el in enumerate(strs):
            if len(el) < len(min_str):
                min_str = el
                min_str_i = i
        return min_str, min_str_i


def main():
    assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
    assert Solution().longestCommonPrefix(["", "", ""]) == ""
    assert Solution().longestCommonPrefix(["dog", ""]) == ""


if __name__ == '__main__':
    main()
