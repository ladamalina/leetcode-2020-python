import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._queue = collections.deque()
        self._map = dict()


    def get(self, key: int) -> int:
        if key in self._map:
            self._queue.remove(key)
            self._queue.appendleft(key)

        return self._map.get(key, -1)


    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self._queue.remove(key)
        elif len(self._map.keys()) >= self._capacity:
            evicted_key = self._queue.pop()
            del self._map[evicted_key]

        self._queue.appendleft(key)
        self._map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def main():
    pass


if __name__ == '__main__':
    main()
