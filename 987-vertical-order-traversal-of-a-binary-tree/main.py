import logging
from typing import List, Optional

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def __init__(self):
        self._x_axis_dict: Dict[int, List[List[int]]] = dict()
        self._min_x = None
        self._max_x = None

    def put(self, x: int, y: int, val: int) -> None:
        point = [y, val]
        if x in self._x_axis_dict:
            self._x_axis_dict[x].append(point)
        else:
            self._x_axis_dict[x] = [point]

        if self._min_x is None or x < self._min_x:
            self._min_x = x
        if self._max_x is None or x > self._max_x:
            self._max_x = x

    def putNode(self, n: Optional[TreeNode], x: int, y: int) -> None:
        if n is None:
            return
        self.put(x, y, n.val)
        self.putNode(n.left, x - 1, y - 1)
        self.putNode(n.right, x + 1, y - 1)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.putNode(root, x=0, y=0)
        slices: List[List[int]] = []
        for x in range(self._min_x, self._max_x + 1):
            points = self._x_axis_dict.get(x, [])
            if not points:
                continue
            points.sort(key=lambda p: (-1 * p[0], p[1]))
            slices.append([_[1] for _ in points])

        return slices


def main():
    pass


if __name__ == '__main__':
    main()
