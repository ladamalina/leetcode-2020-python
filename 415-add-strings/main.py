import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def sumStrings(self, num1: str, num2: str, prev: int, prev_sum: str) -> str:
        logger.debug(f'{num1=}, {num2=}, {prev=}, {prev_sum=}')
        if len(num1) == 0 and len(num2) == 0:
            return str(prev) + prev_sum if prev > 0 else prev_sum

        curr1 = int(num1[-1]) if len(num1) else 0
        curr2 = int(num2[-1]) if len(num2) else 0
        curr_sum = curr1 + curr2 + prev
        curr_big = curr_sum // 10
        curr_small = curr_sum % 10

        left_of_num1 = num1[:-1] if len(num1) else ""
        left_of_num2 = num2[:-1] if len(num2) else ""

        return self.sumStrings(left_of_num1, left_of_num2, curr_big, str(curr_small)) + prev_sum

    def addStrings(self, num1: str, num2: str) -> str:
        logger.debug('-' * 40)
        return self.sumStrings(num1, num2, prev=0, prev_sum="")

def main():
    assert Solution().addStrings("1200", "34") == "1234"
    assert Solution().addStrings("274", "181") == "455"
    assert Solution().addStrings("215", "806") == "1021"
    assert Solution().addStrings("999999", "1") == "1000000"


if __name__ == '__main__':
    main()
