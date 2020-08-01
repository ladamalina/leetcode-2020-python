import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        idx = {idx: i for i, idx in enumerate(indices)}
        return "".join([s[idx[_]] for _ in range(len(indices))])


def main():
    assert Solution().restoreString(s="codeleet", indices=[4,5,6,7,0,2,1,3]) == "leetcode"


if __name__ == '__main__':
    main()
