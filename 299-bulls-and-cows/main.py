import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_cnt = dict()
        for ch in secret:
            if ch in secret_cnt:
                secret_cnt[ch] += 1
            else:
                secret_cnt[ch] = 1

        guess_cnt = dict()
        for ch in guess:
            if ch in guess_cnt:
                guess_cnt[ch] += 1
            else:
                guess_cnt[ch] = 1

        match_chs = set(secret_cnt.keys()).intersection(set(guess_cnt.keys()))
        match_cnt = dict()
        for ch in match_chs:
            match_cnt[ch] = min(secret_cnt[ch], guess_cnt[ch])

        bulls = 0
        for i, ch in enumerate(guess):
            if ch == secret[i]:
                bulls += 1

        cows = sum(match_cnt.values()) - bulls

        return f'{bulls}A{cows}B'


def main():
    assert Solution().getHint("1807", "7810") == "1A3B"
    assert Solution().getHint("1123", "0111") == "1A1B"
    assert Solution().getHint("1", "0") == "0A0B"


if __name__ == '__main__':
    main()
