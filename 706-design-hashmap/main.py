import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class MyHashMap:

    def __init__(self):
        self._l = [-1 for _ in range(1000000 + 1)]

    def put(self, key: int, value: int) -> None:
        self._l[key] = value

    def get(self, key: int) -> bool:
        return self._l[key]

    def remove(self, key: int) -> None:
        self._l[key] = -1


def main():
    pass


if __name__ == '__main__':
    main()
