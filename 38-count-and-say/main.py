import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def countAndSay(self, n: int) -> str:
        first_rows = ["1"]
        if n <= len(first_rows):
            return first_rows[n - 1]

        logger.debug('-' * 40)
        logger.debug(f'{n=}')
        for i in range(len(first_rows), n):
            # generating row #i, idx=i-1
            prev_row = first_rows[i - 1]
            curr_row = ""
            counter = 0
            logger.debug(f'generating row #{i}, {first_rows[i - 1]=}')
            for j, ch in enumerate(prev_row):
                if j == 0:
                    counter += 1
                else:
                    if ch == prev_row[j - 1]:
                        counter += 1
                    else:
                        curr_row += f"{counter}{prev_row[j - 1]}"
                        counter = 1
            curr_row += f"{counter}{prev_row[-1]}"
            first_rows.append(curr_row)

        return first_rows[-1]

def main():
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(10) == "13211311123113112211"


if __name__ == '__main__':
    main()
