import logging
import re
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(0, numRows):
            curr_l = []
            curr_len = i + 1
            for j in range(0, i+1):
                if j == 0 or j == (curr_len - 1):
                    curr_l.append(1)
                else:
                    curr_l.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(curr_l)

        return res


def main():
    assert Solution().generate(5) == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
    assert Solution().generate(1) == [[1]]
    assert Solution().generate(0) == []



if __name__ == '__main__':
    main()
