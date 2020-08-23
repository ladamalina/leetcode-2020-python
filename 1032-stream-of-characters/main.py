import collections
import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class StreamChecker:
    def __init__(self, words: List[str]):
        self.s = ''
        self.d = collections.defaultdict(set)
        for w in words:
            self.d[w[-1]].add(w)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(w) for w in self.d[letter])

def main():
    stream_checker = StreamChecker(["cd","f","kl"])
    assert stream_checker.query('a') is False
    assert stream_checker.query('b') is False
    assert stream_checker.query('c') is False
    assert stream_checker.query('d') is True
    assert stream_checker.query('e') is False
    assert stream_checker.query('f') is True
    assert stream_checker.query('g') is False
    assert stream_checker.query('h') is False
    assert stream_checker.query('i') is False
    assert stream_checker.query('j') is False
    assert stream_checker.query('k') is False
    assert stream_checker.query('l') is True


if __name__ == '__main__':
    main()
