import inspect
import logging
from typing import Dict, List, Tuple

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def isBadVersion(version: int) -> bool:
    pass


versions_g: Dict[int, bool] = dict()


class Solution:
    def checkBad(self, from_n: int, to_n: int) -> int:
        global versions_g
        versions_num = to_n - from_n + 1
        logger.debug(f'{from_n=}, {to_n=}, {versions_num=}')

        if versions_num == 1:
            if from_n not in versions_g:
                versions_g[from_n] = isBadVersion(from_n)
            if versions_g[from_n] is True:  # is bad
                return from_n
            else:
                return from_n - 1

        elif versions_num == 2:
            if from_n not in versions_g:
                versions_g[from_n] = isBadVersion(from_n)
            if to_n not in versions_g:
                versions_g[to_n] = isBadVersion(to_n)

            if versions_g[from_n] is False and versions_g[to_n] is False:  # both are good
                return to_n + 1
            elif versions_g[from_n] is False and versions_g[to_n] is True:
                return to_n
            elif versions_g[from_n] is True and versions_g[to_n] is True:  # both are bad
                return to_n - 1

        else:
            middle_n = from_n + (to_n - from_n) // 2
            if middle_n not in versions_g:
                versions_g[middle_n] = isBadVersion(middle_n)
            logger.debug(f'{middle_n=}, {versions_g[middle_n]=}')
            if versions_g[middle_n] is True:  # middle version is bad
                # check to the left
                return self.checkBad(from_n, middle_n)
            else:  # middle version is good
                # check to the right
                return self.checkBad(middle_n, to_n)


    def firstBadVersion(self, n) -> int:
        """
        :type n: int
        :rtype: int
        """
        global versions_g
        versions_g = dict()

        logger.debug('-' * 40)
        logger.debug(f'{n=}, {versions_g=}')

        return self.checkBad(1, n)


def main():
    for _input in [
        [5, 4],
        [5, 1],
        [2, 1],
        [1, 1],
        [2126753390, 1702766719]
    ]:
        global isBadVersion
        def isBadVersionExpected(version: int) -> bool:
            return version >= _input[1]
        isBadVersion = isBadVersionExpected

        assert Solution().firstBadVersion(_input[0]) == _input[1]


if __name__ == '__main__':
    main()
