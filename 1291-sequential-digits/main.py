import logging
from typing import Generator, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        logger.info('-' * 40)
        logger.info(f'{low=}, {high=}')
        low_len = len(str(low))
        high_len = len(str(high))
        logger.info(f'{low_len=}, {high_len=}')
        nums = []
        for i in range(low_len, high_len + 1):
            seq_of_len = self.seqOfLen(i)
            logger.info(f'{i=}, {seq_of_len=}')
            if seq_of_len is None:
                continue
            num = next(seq_of_len, None)
            while num is not None:
                if low <= num <= high:
                    nums.append(num)
                num = next(seq_of_len, None)
            logger.info(f'{nums=}')

        return nums

    def seqOfLen(self, length: int) -> Generator[int, None, None]:
        if length < 1 or length > 10:
            return
        num = ''
        for i in range(1, length + 1):
            num += str(i)
        diff = int('1' * length)
        while len(num) == length:
            yield int(num)
            if int(num[-1]) == 9:
                break
            num = str(int(num) + diff)

        return None


def main():
    assert Solution().sequentialDigits(100, 300) == [123, 234]
    assert Solution().sequentialDigits(1000, 13000) == [1234,2345,3456,4567,5678,6789,12345]


if __name__ == '__main__':
    main()
