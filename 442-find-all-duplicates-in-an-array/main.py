import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                result.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1

        return result


def main():
    assert Solution().findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]


if __name__ == '__main__':
    main()
