import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str, List[str]] = dict()
        for i in range(0, len(strs)):
            sorted_str = str(sorted(strs[i]))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(strs[i])
            else:
                anagrams[sorted_str] = [strs[i]]

        return list(anagrams.values())


def main():
    pass


if __name__ == '__main__':
    main()
