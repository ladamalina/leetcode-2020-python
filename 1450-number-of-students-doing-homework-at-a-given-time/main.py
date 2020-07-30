import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        num = 0
        for i in range(0, len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                num += 1

        return num


def main():
    assert Solution().busyStudent([4], [4], 4) == 1
    assert Solution().busyStudent([4], [4], 5) == 0
    assert Solution().busyStudent([1,1,1,1], [1,3,2,4], 7) == 0
    assert Solution().busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5) == 5


if __name__ == '__main__':
    main()
