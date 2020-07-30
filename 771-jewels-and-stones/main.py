import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j_set = set()
        for j in J:
            j_set.add(j)

        jewels = 0
        for s in S:
            if s in j_set:
                jewels += 1

        return jewels


def main():
    assert Solution().numJewelsInStones(J="aA", S="aAAbbbb") == 3
    assert Solution().numJewelsInStones(J="z", S="ZZ") == 0


if __name__ == '__main__':
    main()
