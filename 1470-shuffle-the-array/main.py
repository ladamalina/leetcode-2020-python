import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for ni in range(1, n + 1):
            res.append(nums[ni - 1])
            res.append(nums[len(nums) // 2 + ni - 1])

        return res


def main():
    assert Solution().shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
    assert Solution().shuffle([1,2], 1) == [1,2]


if __name__ == '__main__':
    main()
