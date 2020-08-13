import itertools
import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self._init_ch: str = characters
        self._init_list: List[str] = list(characters)
        self._init_len: int = combinationLength
        self._combinations: List[str] = self.combine_chars(self._init_list, self._init_len)
        self._combinations.sort()
        self._idx = 0

    def next(self) -> str:
        next = self._combinations[self._idx]
        self._idx += 1

        return next

    def hasNext(self) -> bool:
        return 0 <= self._idx < len(self._combinations)

    def combine_chars(self, chars: List[str], k: int) -> List[str]:
        return ["".join(_) for _ in list(set(itertools.combinations(chars, k)))]


def main():
    iterator: CombinationIterator = CombinationIterator("abc", 2)
    logger.debug(f"{iterator._combinations=}")
    assert iterator.next() == "ab"
    assert iterator.hasNext() is True
    assert iterator.next() == "ac"
    assert iterator.hasNext() is True
    assert iterator.next() == "bc"
    assert iterator.hasNext() is False


if __name__ == '__main__':
    main()
