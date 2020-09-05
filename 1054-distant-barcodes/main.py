import collections
import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        logger.debug('-' * 40)
        logger.debug(f'{barcodes=}')
        codes_count_dict: Dict[int, int] = dict()
        for code in barcodes:
            if code in codes_count_dict:
                codes_count_dict[code] += 1
            else:
                codes_count_dict[code] = 1
        logger.debug(f'{codes_count_dict=}')
        codes_count_list: List[List[int]] = [[_, codes_count_dict[_]] for _ in codes_count_dict]
        codes_count_list.sort(key=lambda x: x[1], reverse=True)
        logger.debug(f'{codes_count_list=}')

        buckets: List[List[int]] = [[] for _ in range(codes_count_list[0][1])]
        logger.debug(f'{buckets=}')
        bucket_i = 0
        for code_i in range(len(codes_count_list)):
            code = codes_count_list[code_i][0]
            code_count = codes_count_list[code_i][1]
            logger.debug(f'{code=}, {code_count=}')
            for j in range(code_count):
                buckets[bucket_i].append(code)
                bucket_i = 0 if bucket_i >= len(buckets) - 1 else bucket_i + 1
                logger.debug(f'{buckets=}')

        result: List[int] = []
        for k in range(len(buckets)):
            result += buckets[k]
        logger.debug(f'{result=}')

        return result


def main():
    assert Solution().rearrangeBarcodes([1,1,1,2,2,2]) == [1, 2, 1, 2, 1, 2]
    assert Solution().rearrangeBarcodes([1,1,1,1,2,2,3,3]) == [1, 2, 1, 2, 1, 3, 1, 3]


if __name__ == '__main__':
    main()
