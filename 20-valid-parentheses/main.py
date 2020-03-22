class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"}": "{", ")": "(", "]": "["}
        seen_stack = []
        for ch in s:
            if ch in braces:
                if seen_stack:
                    if braces.get(ch) == seen_stack[-1]:
                        seen_stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                seen_stack.append(ch)

        return False if seen_stack else True


def main():
    assert Solution().isValid("(") == False
    assert Solution().isValid("()") == True
    assert Solution().isValid("()") == True
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("{[]}") == True


if __name__ == '__main__':
    main()
