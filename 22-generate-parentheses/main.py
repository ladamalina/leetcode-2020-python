import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def close_p(el: dict) -> dict:
    return {
        "p": f'{el["p"]})',
        "opened": el["opened"] - 1,
        "left": el["left"]
    }


def open_p(el: dict) -> dict:
    return {
        "p": f'{el["p"]}(',
        "opened": el["opened"] + 1,
        "left": el["left"] - 1
    }


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        results = [{"p": "(", "opened": 1, "left": n-1}]
        for _ in range(1, n*2):
            for i, r in enumerate(results):
                if r["left"] > 0 and r["opened"] == 0:
                    results[i] = open_p(r)
                elif r["left"] == 0 and r["opened"] > 0:
                    results[i] = close_p(r)
                elif r["left"] > 0 and r["opened"] > 0:
                    results[i] = open_p(r)
                    results.append(close_p(r))
                else:  # r["left"] == 0 and r["opened"] == 0:
                    continue

        return sorted([_["p"] for _ in results])


def main():
    assert Solution().generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]


if __name__ == '__main__':
    main()
