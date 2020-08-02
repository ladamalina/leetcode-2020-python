import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._l = [False for _ in range(1000000 + 1)]

    def add(self, key: int) -> None:
        self._l[key] = True

    def remove(self, key: int) -> None:
        self._l[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self._l[key]


def main():
    pass


if __name__ == '__main__':
    main()
