import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = set()
        same = set()
        for i, n in enumerate(arr):
            if n * 2 in same or n in doubles:
                return True
            else:
                doubles.add(n * 2)
                same.add(n)

        return False


def main():
    assert Solution().checkIfExist([10,2,5,3]) is True
    assert Solution().checkIfExist([7,1,14,11]) is True
    assert Solution().checkIfExist([7,1,7,11]) is False
    assert Solution().checkIfExist([3,1,7,11]) is False


if __name__ == '__main__':
    main()
