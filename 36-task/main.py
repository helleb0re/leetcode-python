from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    row_checker = [set() for _ in range(9)]
    column_checker = [set() for _ in range(9)]
    main_ceil_checker = [set() for _ in range(9)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                continue

            value = board[i][j]
            main_ceil_index = i // 3 * 3 + j // 3
            if (
                value in row_checker[i]
                or value in column_checker[j]
                or value in main_ceil_checker[main_ceil_index]
            ):
                return False

            row_checker[i].add(value)
            column_checker[j].add(value)
            main_ceil_checker[main_ceil_index].add(value)

    return True


if __name__ == "__main__":
    assert isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
    assert not isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
