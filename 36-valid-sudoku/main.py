import logging
from typing import List

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Solution:
    def isValidBlock(self, lists: List[List[str]]) -> bool:
        seen_nums = set()
        for l in lists:
            for num in l:
                if num == ".":
                    continue
                if num in seen_nums:
                    return False
                seen_nums.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for l in board:
            if not self.isValidBlock([l, ]):
                return False

        # check columns
        for i in range(0, 9):
            column = [_[i] for _ in board]
            if not self.isValidBlock([column, ]):
                return False

        # check blocks
        for i in [(0,2), (3,5), (6,8)]:
            for j in [(0,2), (3,5), (6,8)]:
                lines = [
                    l[j[0]:j[1]+1]
                    for l in board[i[0]:i[1]+1]
                ]
                if not self.isValidBlock(lines):
                    return False
        return True


def main():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert Solution().isValidSudoku(board) == True

    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert Solution().isValidSudoku(board) == False


if __name__ == '__main__':
    main()
