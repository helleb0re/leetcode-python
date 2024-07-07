from typing import List, Set


# recursion
def exist(board: List[List[str]], word: str) -> bool:
    backtracking_result = False

    def launch_backtracking(
        i: int, j: int, curr_word_idx: int = 0, explored: Set[tuple] = set()
    ):
        explored = explored | {(i, j)}

        if board[i][j] != word[curr_word_idx]:
            return

        if curr_word_idx == len(word) - 1:
            nonlocal backtracking_result
            backtracking_result = True
            return

        # left
        if j - 1 >= 0 and (i, j - 1) not in explored:
            launch_backtracking(i, j - 1, curr_word_idx + 1, explored)
        # up
        if i - 1 >= 0 and (i - 1, j) not in explored:
            launch_backtracking(i - 1, j, curr_word_idx + 1, explored)
        # down
        if i + 1 < len(board) and (i + 1, j) not in explored:
            launch_backtracking(i + 1, j, curr_word_idx + 1, explored)
        # right
        if j + 1 < len(board[i]) and (i, j + 1) not in explored:
            launch_backtracking(i, j + 1, curr_word_idx + 1, explored)

    for i in range(len(board)):
        for j in range(len(board[i])):
            launch_backtracking(i, j)
            if backtracking_result:
                return True

    return False


# iteration
def exist(board: List[List[str]], word: str) -> bool:
    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] != word[0]:
                continue

            buffer = [((row_idx, col_idx), 0, {(row_idx, col_idx)})]

            while buffer:
                (i, j), curr_word_letter_idx, explored = buffer.pop()

                if curr_word_letter_idx == len(word) - 1:
                    return True

                # left
                if (
                    j - 1 >= 0
                    and board[i][j - 1] == word[curr_word_letter_idx + 1]
                    and (i, j - 1) not in explored
                ):
                    buffer.append(
                        ((i, j - 1), curr_word_letter_idx + 1, explored | {(i, j - 1)})
                    )
                # up
                if (
                    i - 1 >= 0
                    and board[i - 1][j] == word[curr_word_letter_idx + 1]
                    and (i - 1, j) not in explored
                ):
                    buffer.append(
                        ((i - 1, j), curr_word_letter_idx + 1, explored | {(i - 1, j)})
                    )
                # down
                if (
                    i + 1 < len(board)
                    and board[i + 1][j] == word[curr_word_letter_idx + 1]
                    and (i + 1, j) not in explored
                ):
                    buffer.append(
                        ((i + 1, j), curr_word_letter_idx + 1, explored | {(i + 1, j)})
                    )
                # right
                if (
                    j + 1 < len(board[i])
                    and board[i][j + 1] == word[curr_word_letter_idx + 1]
                    and (i, j + 1) not in explored
                ):
                    buffer.append(
                        ((i, j + 1), curr_word_letter_idx + 1, explored | {(i, j + 1)})
                    )

    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED")
    assert exist(board, "SEE")
    assert not exist(board, "ABCD")
    assert exist([["a", "b"]], "ba")
    assert not exist([["a", "a"]], "aaa")
