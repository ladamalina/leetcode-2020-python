import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        logger.debug('-' * 40)
        logger.debug(f'{n=}')
        nums = [True for _ in range(0, n)]
        nums[0] = False
        nums[1] = False
        for num in range(2, n):
            multi = 2
            while num * multi < n:
                nums[num * multi] = False
                multi += 1
        logger.debug(f'{nums=}')
        count = 0
        for i, is_prime in enumerate(nums):
            if i > 1 and is_prime:
                count += 1

        return count

def main():
    assert Solution().countPrimes(10) == 4


if __name__ == '__main__':
    main()
