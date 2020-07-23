import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def defangIPaddr(self, address: str) -> str:
        for i in range(len(address) - 1, -1, -1):
            if address[i] != ".":
                continue
            address = address[:i] + "[.]" + address[i + 1:]
        return address


def main():
    assert Solution().defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"


if __name__ == '__main__':
    main()
