import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_strs: List[str] = []
        curr_balance = 0
        begin_idx = 0
        for i, ch in enumerate(s):
            if ch == "L":
                curr_balance -= 1
            elif ch == "R":
                curr_balance += 1
            if curr_balance == 0:
                balanced_strs.append(s[begin_idx:i + 1])
                begin_idx = i + 1
        if curr_balance != 0:
            balanced_strs.append(s[begin_idx:len(s)])

        return len(balanced_strs)


def main():
    assert Solution().balancedStringSplit("RLRRLLRLRL") == 4
    assert Solution().balancedStringSplit("RLLLLRRRLR") == 3
    assert Solution().balancedStringSplit("LLLLRRRR") == 1
    assert Solution().balancedStringSplit("RL") == 1


if __name__ == '__main__':
    main()
