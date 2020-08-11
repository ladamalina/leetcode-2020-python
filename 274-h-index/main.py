import inspect
import logging
from typing import Dict, List, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution(object):
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0


def main():
    assert Solution().hIndex([3,0,6,1,5]) == 3


if __name__ == '__main__':
    main()
