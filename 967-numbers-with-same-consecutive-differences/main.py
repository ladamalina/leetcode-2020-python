import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def numsSameConsecDiff(self, N, K):
        if N == 1:
            return list(range(10))
        result = []

        def dfs(prev, number):
            if len(number) == N:
                result.append(int(number))
                return
            for digit in range(10):
                if prev is None and digit == 0:
                    continue
                if prev is None or abs(digit-prev) == K:
                    dfs(digit, number + str(digit))

        dfs(None, '')
        return result


def main():
    assert Solution().numsSameConsecDiff(1, 0) == [0,1,2,3,4,5,6,7,8,9]
    assert Solution().numsSameConsecDiff(1, 1) == [0,1,2,3,4,5,6,7,8,9]
    assert Solution().numsSameConsecDiff(1, 6) == [0,1,2,3,4,5,6,7,8,9]
    assert Solution().numsSameConsecDiff(3, 0) == [111,222,333,444,555,666,777,888,999]
    assert Solution().numsSameConsecDiff(3, 7) == [181,292,707,818,929]
    assert Solution().numsSameConsecDiff(2, 1) == [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


if __name__ == '__main__':
    main()
