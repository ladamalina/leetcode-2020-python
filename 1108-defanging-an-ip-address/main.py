import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = {_: 0 for _ in arr2}
        other = []
        for a1 in arr1:
            if a1 in counter:
                counter[a1] += 1
            else:
                other.append(a1)
        result = []
        for a2 in arr2:
            result.extend([a2] * counter[a2])
        result.extend(sorted(other))

        return result


def main():
    assert Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]


if __name__ == '__main__':
    main()
