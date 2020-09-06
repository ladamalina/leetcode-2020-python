import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set([_[0] for _ in paths])
        destinations = set([_[1] for _ in paths])

        return list(destinations - sources)[0]


def main():
    assert Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo"
    assert Solution().destCity([["B","C"],["D","B"],["C","A"]]) == "A"


if __name__ == '__main__':
    main()
