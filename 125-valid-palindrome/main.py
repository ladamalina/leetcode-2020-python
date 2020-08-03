import logging
import re
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        logger.debug("-" * 40)
        s_clean = re.sub(r'([^a-zA-Z])+', '', s)
        s_clean = s_clean.lower()
        logger.debug(f"{s=}, {s_clean=}")
        half = len(s_clean) // 2
        for i in range(0, half):
            if s_clean[i] != s_clean[len(s_clean) - i - 1]:
                return False

        return True


def main():
    assert Solution().isPalindrome("") is True
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    assert Solution().isPalindrome("race a car") is False
    assert Solution().isPalindrome("Казак") is True
    assert Solution().isPalindrome("А роза упала на лапу Азора") is True
    assert Solution().isPalindrome("Madam, I’m Adam") is True
    assert Solution().isPalindrome("Do geese see God?") is True
    assert Solution().isPalindrome("a") is True
    assert Solution().isPalindrome("ab_a") is True


if __name__ == '__main__':
    main()
