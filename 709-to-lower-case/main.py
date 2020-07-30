import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def toLowerCase(self, st: str) -> str:
        ch = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}
        res = ''
        for i, s in enumerate(st):
            if s in ch:
                res += ch[s]
            else:
                res += s

        return res

def main():
    assert Solution().toLowerCase("Hello") == "hello"
    assert Solution().toLowerCase("here") == "here"
    assert Solution().toLowerCase("LOVELY") == "lovely"


if __name__ == '__main__':
    main()
