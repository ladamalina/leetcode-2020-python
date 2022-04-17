import logging
import heapq
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MinStack:
    def __init__(self):
        self._stack = []
        self._heap = []
        heapq.heapify(self._heap)

    def push(self, x: int) -> None:
        self._stack.append(x)
        heapq.heappush(self._heap, x)

    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
            self._heap = self._stack[:]
            heapq.heapify(self._heap)

    def top(self) -> int:
        return self._stack[-1] if self._stack else None

    def getMin(self) -> int:
        return heapq.nsmallest(1, self._heap)[0] if self._stack else None


def main():
    ms = MinStack()
    assert ms.push(-2) is None
    assert ms.push(0) is None
    assert ms.push(-3) is None
    assert ms.getMin() == -3
    assert ms.pop() is None
    assert ms.top() == 0
    assert ms.getMin() == -2

    ms = MinStack()
    assert ms.push(-2) is None
    assert ms.push(0) is None
    assert ms.push(-1) is None
    assert ms.getMin() == -2
    assert ms.top() == -1
    assert ms.pop() is None
    assert ms.getMin() == -2



if __name__ == '__main__':
    main()
