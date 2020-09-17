import collections
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx, dy, x, y = 0, 1, 0, 0
        for l in 4*instructions:
            if l == "G":
                x, y = x+dx, y+dy
            elif l == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return (x,y) == (0,0)


def main():
    assert Solution().isRobotBounded("GGLLGG") is True
    assert Solution().isRobotBounded("GL") is True
    assert Solution().isRobotBounded("GG") is False


if __name__ == '__main__':
    main()
