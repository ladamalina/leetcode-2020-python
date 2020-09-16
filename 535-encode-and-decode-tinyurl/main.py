import logging
import random, string

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Codec:
    def __init__(self) -> None:
        self._long = dict()
        self._short = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self._long:
            return self._long.get(longUrl)

        shortUrl = None
        while shortUrl in self._short:
            shortUrl = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        self._long[longUrl] = shortUrl
        self._short[shortUrl] = longUrl

        return self._long.get(longUrl)


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self._short.get(shortUrl)


def main():
    codec = Codec()
    assert codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")) == "https://leetcode.com/problems/design-tinyurl"


if __name__ == '__main__':
    main()
