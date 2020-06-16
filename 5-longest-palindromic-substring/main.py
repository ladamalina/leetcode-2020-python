import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len == 0:
            return ""
        if s_len == 1:
            return s

        potential = []
        for i, ch in enumerate(s):
            if i < s_len-1 and ch == s[i+1]:
                # this char may be in the middle of EVEN palindrome
                potential.append({"i": i, "r": 2})
            if 0 < i < s_len-1 and s[i-1] == s[i+1]:
                # this char may be in the middle of ODD palindrome
                potential.append({"i": i, "r": 1})
        # logger.debug([self.printPotential(s, _["i"]) for _ in potential])

        if not potential:
            return s[0]

        longest_str = ''
        longest_len = 0
        for p in potential:
            # logger.debug(f'Check p={p}')
            left_ch_i = p["i"] if p["r"] == 2 else p["i"] - 1
            right_ch_i = p["i"] + 1
            while 0 <= left_ch_i < s_len and 0 <= right_ch_i < s_len and s[left_ch_i] == s[right_ch_i]:
                palindrome = s[left_ch_i:right_ch_i+1]
                palindrome_len = right_ch_i - left_ch_i + 1
                if palindrome_len > longest_len:
                    # logger.debug(f'Found palindrome={palindrome}, left_ch_i={left_ch_i}, right_ch_i={right_ch_i}')
                    longest_str = palindrome
                    longest_len = palindrome_len

                left_ch_i -= 1
                right_ch_i += 1
                # logger.debug(f'Next: left_ch_i={left_ch_i}, right_ch_i={right_ch_i}')

        return longest_str

    def printPotential(self, s: str, idx: int):
        output = ""
        for i, ch in enumerate(s):
            if i == idx:
                output = f'{output}[{s[i]}]'
            else:
                output = f'{output}{s[i]}'

        return output


def main():
    assert (Solution().longestPalindrome("babad") == "bab" or Solution().longestPalindrome("babad") == "aba")
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("ac") == "a"
    assert Solution().longestPalindrome("aaaa") == "aaaa"


if __name__ == '__main__':
    main()
