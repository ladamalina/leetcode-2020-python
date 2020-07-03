import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

known_paths: Dict[int, int] = dict()

class Solution:
    def climbStairs(self, n: int) -> int:
        # Each time you can either climb 1 or 2 steps.
        if n == 1:
            return 1
        elif n == 2:
             return 1 + self.climbStairs(n - 1)
        else:
            # n > 2
            if n - 1 not in known_paths:
                known_paths[n - 1] = self.climbStairs(n - 1)
            prev = known_paths[n - 1]

            if n - 2 not in known_paths:
                known_paths[n - 2] = self.climbStairs(n - 2)
            prev_prev = known_paths[n - 2]

            return prev + prev_prev


def main():
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5



if __name__ == '__main__':
    main()
