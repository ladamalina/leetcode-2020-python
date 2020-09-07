import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        logger.debug('-' * 40)
        logger.debug(f'{pattern=}, {s=}')
        words = s.split()
        logger.debug(f'{words=}, {len(words)=}, {len(pattern)=}')
        if len(words) != len(pattern):
            return False

        pattern_dict: Dict[str, str] = dict()
        pattern_dict_reversed: Dict[str, str] = dict()
        for i, ch in enumerate(pattern):
            if ch in pattern_dict:
                if pattern_dict[ch] != words[i]:
                    return False
            else:
                found_word = words[i]
                if found_word in pattern_dict_reversed:
                    return False
                pattern_dict[ch] = found_word
                pattern_dict_reversed[found_word] = ch

        return True


def main():
    assert Solution().wordPattern("abba", "dog cat cat dog") is True
    assert Solution().wordPattern("abba", "dog cat cat fish") is False
    assert Solution().wordPattern("aaaa", "dog cat cat dog") is False
    assert Solution().wordPattern("abba", "dog dog dog dog") is False


if __name__ == '__main__':
    main()
