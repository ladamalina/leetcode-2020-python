import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(0, len(nums)):
            target.insert(index[i], nums[i])

        return target


def main():
    assert Solution().createTargetArray([0,1,2,3,4], [0,1,2,2,1]) == [0,4,1,3,2]


if __name__ == '__main__':
    main()
