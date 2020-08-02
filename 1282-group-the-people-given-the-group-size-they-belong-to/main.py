import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class GroupSet:
    def __init__(self):
        self._filling: Dict[int, List[int]] = dict()
        self._filled: List[List[int]] = []

    def put(self, group_size: int, idx: int) -> None:
        if group_size in self._filling:
            self._filling[group_size].append(idx)
        else:
            self._filling[group_size] = [idx]
        if len(self._filling[group_size]) == group_size:
            self._filled.append(self._filling[group_size])
            del self._filling[group_size]

    def get_groups(self) -> List[List[int]]:
        return self._filled


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_set = GroupSet()
        for idx, group_size in enumerate(groupSizes):
            group_set.put(group_size, idx)

        return group_set.get_groups()


def main():
    pass


if __name__ == '__main__':
    main()
