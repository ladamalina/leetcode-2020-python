class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr_ch = dict()  # char: index
        substr_len = 0
        max_substr_len = 0
        for i, ch in enumerate(s):
            if ch in substr_ch:
                ch_prev_i = substr_ch[ch]
                substr_ch_upd = dict()
                substr_len_upd = 0
                for seen_ch in substr_ch:
                    if substr_ch[seen_ch] > ch_prev_i:
                        substr_ch_upd[seen_ch] = substr_ch[seen_ch]
                        substr_len_upd += 1
                substr_ch_upd[ch] = i
                substr_len_upd += 1

                substr_ch = substr_ch_upd
                substr_len = substr_len_upd

            else:
                substr_ch[ch] = i
                substr_len += 1

            if substr_len > max_substr_len:
                max_substr_len = substr_len

        return max_substr_len


def main():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("") == 0


if __name__ == '__main__':
    main()
