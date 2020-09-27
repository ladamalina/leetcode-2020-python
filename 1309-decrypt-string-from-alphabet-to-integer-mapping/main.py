import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                code = int(s[i-2:i]) - 1
                i -= 3
            else:
                code = int(s[i]) - 1
                i -= 1
            res = f"{alpha[code]}{res}"

        return res


def main():
    assert Solution().freqAlphabets("10#11#12") == "jkab"
    assert Solution().freqAlphabets("1326#") == "acz"
    assert Solution().freqAlphabets("25#") == "y"
    assert Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#") == "abcdefghijklmnopqrstuvwxyz"


if __name__ == '__main__':
    main()
