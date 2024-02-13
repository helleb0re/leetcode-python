from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    buffer = []  # monotonic decreasing stack
    for i in range(len(temperatures)):
        while buffer and temperatures[buffer[-1]] < temperatures[i]:
            idx = buffer.pop()
            res[idx] = i - idx
        buffer.append(i)

    return res


if __name__ == "__main__":
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
    assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert dailyTemperatures([30, 60, 90]) == [1, 1, 0]
