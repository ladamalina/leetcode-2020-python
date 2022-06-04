import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        from_i = None
        to_i = None
        logger.debug('-' * 40)
        logger.debug(f'{chars=}')
        for i in range(len(chars) - 1, -1, -1):
            if i == len(chars) - 1:
                to_i = i
            if i == 0:
                from_i = i
            if to_i is None:
                to_i = i
            if i - 1 >= 0 and chars[i - 1] != chars[i]:
                from_i = i
            logger.debug(f'{chars=}, {i=}, {chars[i]=}, {from_i=}, {to_i=}')
            if from_i is not None and to_i is not None:
                ch = chars[from_i]
                count = to_i - from_i + 1
                if count > 1:
                    for j in range(to_i, from_i - 1, -1):
                        if j == from_i:
                            continue
                        elif j == from_i + 1:
                            chars.pop(j)
                            count_chars = str(count)
                            if len(count_chars) == 1:
                                chars.insert(j, count_chars)
                            else:
                                for k in range(0, len(count_chars)):
                                    chars.insert(j + k, count_chars[k])
                        else:  # from_i + 1 < j <= to_i
                            chars.pop(j)
                to_i = None
                from_i = None

        return len(chars)

def main():
    inp = ["a", "a", "b", "b", "c", "c", "c"]
    assert Solution().compress(inp) == 6
    assert inp == ["a", "2", "b", "2", "c", "3"]

    inp = ["a"]
    assert Solution().compress(inp) == 1
    assert inp == ["a"]

    inp = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert Solution().compress(inp) == 4
    assert inp == ["a", "b", "1", "2"]


if __name__ == '__main__':
    main()
