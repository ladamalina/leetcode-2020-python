import logging
from itertools import combinations_with_replacement
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        for i in range(target // max(candidates), target // min(candidates) + 1):
            result += [comb for comb in combinations_with_replacement(candidates, i) if sum(comb) == target]

        return result

def main():
    assert Solution().combinationSum([2,3,6,7], 7) == [7,5,8,12,3,10,9,4,11,6]
    assert Solution().combinationSum([2,3,5], 8) == [[3,5],[2,3,3],[2,2,2,2]]
    assert Solution().combinationSum([7,5,8,12,3,10,9,4,11,6], 21) == [[12,9],[10,11],[7,7,7],[7,5,9],[7,8,6],[7,3,11],[7,10,4],[5,5,11],[5,8,8],[5,12,4],[5,10,6],[8,3,10],[8,9,4],[12,3,6],[3,9,9],[9,6,6],[4,11,6],[7,7,3,4],[7,5,5,4],[7,5,3,6],[7,8,3,3],[7,4,4,6],[5,5,5,6],[5,5,8,3],[5,8,4,4],[5,3,3,10],[5,3,9,4],[5,4,6,6],[8,3,4,6],[12,3,3,3],[3,3,9,6],[3,3,4,11],[3,10,4,4],[3,6,6,6],[9,4,4,4],[7,5,3,3,3],[7,3,3,4,4],[5,5,5,3,3],[5,5,3,4,4],[5,3,3,4,6],[5,4,4,4,4],[8,3,3,3,4],[3,3,3,3,9],[3,3,3,6,6],[3,4,4,4,6],[5,3,3,3,3,4],[3,3,3,3,3,6],[3,3,3,4,4,4],[3,3,3,3,3,3,3]]


if __name__ == '__main__':
    main()
