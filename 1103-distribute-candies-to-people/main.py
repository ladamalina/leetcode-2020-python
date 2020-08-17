import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        logger.debug("-" * 40)
        logger.debug(f"{candies=}, {num_people=}")
        turn = 0
        candies_left = candies
        row_sum = lambda n, turn: sum(range(n * turn + 1, n * turn + n + 1))
        logger.debug(f"{turn=}, {candies_left=}, {row_sum(num_people, turn)=}")
        while row_sum(num_people, turn) <= candies_left:
            candies_left -= row_sum(num_people, turn)
            turn += 1
            logger.debug(f"{turn=}, {candies_left=}, {row_sum(num_people, turn)=}")
        logger.debug(f"Round 1 finished with {turn=}, {candies_left=}")

        i_need_candies = lambda i, n: 1 + i + turn * n
        i = 0
        logger.debug(f"{i=}, {candies_left=}, {i_need_candies(i, num_people)=}")
        while i_need_candies(i, num_people) <= candies_left:
            candies_left -= i_need_candies(i, num_people)
            i += 1
            logger.debug(f"{i=}, {candies_left=}, {i_need_candies(i, num_people)=}")
        logger.debug(f"Round 2 finished with {i=}, {candies_left=}")

        candies_range = [_ + 1 for _ in range(i_need_candies(i, num_people) - 1)] + [candies_left]
        logger.debug(f"{candies_range=}")
        num_candies = [0] * num_people
        for j in range(num_people):
            num_candies[j] = sum(candies_range[j::num_people])
        logger.debug(f"{num_candies=}")

        return num_candies

def main():
    assert Solution().distributeCandies(60, 4) == [15,18,15,12]
    assert Solution().distributeCandies(7, 4) == [1,2,3,1]
    assert Solution().distributeCandies(10, 3) == [5,2,3]


if __name__ == '__main__':
    main()
