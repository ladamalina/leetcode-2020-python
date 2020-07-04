import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        c3 = 0
        c5 = 0
        for i in range(1, n + 1):
            c3 = c3 + 1 if c3 + 1 <= 3 else 1
            c5 = c5 + 1 if c5 + 1 <= 5 else 1
            if c3 != 3 and c5 != 5:
                l.append(str(i))
                continue
            s = ""
            if c3 == 3:
                s += "Fizz"
            if c5 == 5:
                s += "Buzz"
            l.append(s)

        return l

def main():
    assert Solution().fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
    assert Solution().fizzBuzz(1) == ["1"]
    assert Solution().fizzBuzz(0) == []


if __name__ == '__main__':
    main()
