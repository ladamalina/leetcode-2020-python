import collections
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            chars = collections.defaultdict(int)
            for ch in A:
                chars[ch] += 1
                if chars[ch] > 1:
                    return True
            return False

        # A != B
        i1 = None
        i2 = None
        for i in range(len(A)):
            if A[i] != B[i]:
                if i1 is None:
                    i1 = i
                    continue
                # i1 is not None
                if i2 is None:
                    i2 = i
                    continue
                # i1 is not None and i2 is not None
                return False
        if i1 is None or i2 is None:
            return False

        return A[i1] == B[i2] and A[i2] == B[i1]


def main():
    assert Solution().buddyStrings(A = "ab", B = "ba") is True
    assert Solution().buddyStrings(A = "ab", B = "ab") is False
    assert Solution().buddyStrings(A = "aa", B = "aa") is True
    assert Solution().buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb") is True
    assert Solution().buddyStrings(A = "", B = "aa") is False


if __name__ == '__main__':
    main()
