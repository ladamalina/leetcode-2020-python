import logging
from typing import Dict, List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        logging.debug('-' * 40)
        logging.debug(f'{S=}')
        char_to_interval: Dict[str, List[int]] = dict()
        chars_order: List[str] = []
        for i, ch in enumerate(S):
            if ch in char_to_interval:
                char_to_interval[ch][1] = i
            else:
                char_to_interval[ch] = [i, i]
                chars_order.append(ch)
        logging.debug(f'{chars_order=}, {char_to_interval=}')

        # non-overlappinng partition
        partition: List[List[int]] = [char_to_interval[chars_order[0]]]
        logging.debug(f'{partition=}')
        for interval_i in range(1, len(chars_order)):
            current_char = chars_order[interval_i]
            current_interval = char_to_interval[current_char]
            last_interval = partition[-1]

            if current_interval[0] > last_interval[1]:
                # start of new part
                partition.append(current_interval)
            else:
                # extend last_interval
                partition[-1][1] = max(last_interval[1], current_interval[1])
        logging.debug(f'{partition=}')

        result = [_[1] - _[0] + 1 for _ in partition]
        return result


def main():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9,7,8]
    assert Solution().partitionLabels("a") == [1]


if __name__ == '__main__':
    main()
