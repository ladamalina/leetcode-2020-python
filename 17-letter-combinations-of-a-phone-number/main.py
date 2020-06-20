import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        logger.debug(f'digits={digits}')
        digit_to_chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []
        for d in digits:
            if result:
                new_result = []
                for r in result:
                    for ch in digit_to_chars.get(d):
                        new_result.append(f'{r}{ch}')
                result = new_result
            else:
                result = digit_to_chars.get(d)[:]
        logger.debug(f'result={result}')

        return result


def main():
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations("2") == ["a", "b", "c"]


if __name__ == '__main__':
    main()
