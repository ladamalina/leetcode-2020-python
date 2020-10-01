import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class RecentCounter:

    def __init__(self):
        self._recent_calls: List[int] = []

    def ping(self, t: int) -> int:
        self._recent_calls = [_ for _ in self._recent_calls if t-3000 <= _ <= t]
        self._recent_calls.append(t)

        return len(self._recent_calls)


def main():
    pass


if __name__ == '__main__':
    main()
