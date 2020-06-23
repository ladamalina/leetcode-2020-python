import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
                if nums[i] == val:
                    nums.pop(i)
        return len(nums)


def main():
    l = [1,1,1,2,2,3]
    assert Solution().removeElement(l, 1) == 3
    assert l == [2,2,3]

    l = [2,2]
    assert Solution().removeElement(l, 2) == 0
    assert l == []

    l = [2,3]
    assert Solution().removeElement(l, 1) == 2
    assert l == [2,3]

    l = [1]
    assert Solution().removeElement(l, 1) == 0
    assert l == []

    l = [1]
    assert Solution().removeElement(l, 2) == 1
    assert l == [1]


if __name__ == '__main__':
    main()
