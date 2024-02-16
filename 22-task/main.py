from typing import List


def generateParenthesis(n: int) -> List[str]:
    max_len = 2 * n
    buffer = [("(", 1, 1)]
    res = []
    while buffer:
        seq, vacancy_for_close, num_open_bracket = buffer.pop()

        if vacancy_for_close == 0 and len(seq) == max_len:
            res.append(seq)
        else:
            if vacancy_for_close > 0:
                buffer.append((seq + ")", vacancy_for_close - 1, num_open_bracket))

            if num_open_bracket != n:
                buffer.append((seq + "(", vacancy_for_close + 1, num_open_bracket + 1))

    return res


if __name__ == "__main__":
    assert generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert generateParenthesis(1) == ["()"]
