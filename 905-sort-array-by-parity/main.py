import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even: List[int] = [_ for _ in A if _ % 2 == 0]
        odd: List[int] = [_ for _ in A if _ % 2 == 1]

        return even + odd


def main():
    assert Solution().sortArrayByParity([3,1,2,4]) == [2,4,3,1]


if __name__ == '__main__':
    main()
