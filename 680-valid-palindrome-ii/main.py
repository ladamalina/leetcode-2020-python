import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def validPalindrome(self, s: str) -> bool:
        logger.debug("-" * 40)
        logger.debug(f"{s=}")
        if len(s) <= 1:
            return True

        il = 0
        ir = len(s) - 1
        i_to_del = None

        while il < ir:
            logger.debug(f"{il=}, {s[:il + 1]=}, {ir=}, {s[ir:]=}")
            if s[il] == s[ir]:
                il += 1
                ir -= 1
                continue

            # s[il] != s[ir]
            if i_to_del is not None:
                return False

            if s[il + 1] == s[ir]:
                if il + 2 <= ir - 1:
                    if s[il + 2] == s[ir - 1]:
                        i_to_del = il
                        il += 3
                        ir -= 2
                        continue
                else:
                    i_to_del = il
                    il += 2
                    ir -= 1
                    continue

            if s[il] == s[ir - 1]:
                if il + 1 <= ir - 2:
                    if s[il + 1] == s[ir - 2]:
                        i_to_del = ir
                        il += 2
                        ir -= 3
                        continue
                else:
                    i_to_del = ir
                    il += 1
                    ir -= 2
                    continue

            return False

        return True

def main():
    assert Solution().validPalindrome("aba") is True
    assert Solution().validPalindrome("abca")is True
    assert Solution().validPalindrome("a") is True
    assert Solution().validPalindrome("ab") is True
    assert Solution().validPalindrome("abc") is False
    assert Solution().validPalindrome("aac") is True
    assert Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") is True
    assert Solution().validPalindrome("ebcbbececabbacecbbcbe") is True


if __name__ == '__main__':
    main()
