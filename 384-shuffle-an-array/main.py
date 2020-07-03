import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:

    def __init__(self, nums: List[int]):
        self._origin = nums[:]
        self._nums = nums


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self._origin


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self._nums)

        return self._nums


def main():
    pass


if __name__ == '__main__':
    main()
