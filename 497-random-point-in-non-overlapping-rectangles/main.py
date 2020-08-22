import logging
import random
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:

    def __init__(self, rects: List[List[int]]):
        self._rects = rects
        self._areas = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]

    def pick(self) -> List[int]:
        x1, y1, x2, y2 = random.choices(population=self._rects, weights=self._areas, k=1)[0]
        return [random.randint(x1, x2), random.randint(y1, y2)]


def main():
    pass


if __name__ == '__main__':
    main()
