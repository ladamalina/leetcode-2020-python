import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        if len(points) <= 1:
            return 1
        points = sorted(points)
        arrows = 0
        while points:
            last_id = 0
            overlap = points[0]
            for i in range(1, len(points)):
                overlap = [max(overlap[0], points[i][0]), min(overlap[1], points[i][1])]
                if overlap[0] <= overlap[1]:
                    last_id = i
                else:
                    break
            points = points[last_id + 1:]
            arrows += 1
        return arrows


def main():
    assert Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
    assert Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
    assert Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2
    assert Solution().findMinArrowShots([[1,2]]) == 1
    assert Solution().findMinArrowShots([[2,3],[2,3]]) == 1
    assert Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]) == 2


if __name__ == '__main__':
    main()
