import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)

        return False


def main():
    assert Solution().containsDuplicate([1,2,3,1]) == True
    assert Solution().containsDuplicate([1,2,3,4]) == False
    assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    assert Solution().containsDuplicate([]) == False
    assert Solution().containsDuplicate([1]) == False
    assert Solution().containsDuplicate([1,1]) == True


if __name__ == '__main__':
    main()
