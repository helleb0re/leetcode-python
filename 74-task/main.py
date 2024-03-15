from typing import List


# class Index:
#     def __init__(self, idx : int):
#         self.idx = idx

#     def getMarkerIndex(self, rows: int, cols: int):
#         return self.idx // cols, self.idx % cols


def getMatrixValue(matrix: List[List[int]], index: int) -> int:
    if not matrix or not matrix[0]:
        raise RuntimeError

    n = len(matrix[0])
    return index // n, index % n


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1

    while l <= r:
        mid = (l + r) // 2
        mid_value = matrix[mid // n][mid % n]

        if mid_value < target:
            l = mid + 1
        elif mid_value > target:
            r = mid - 1
        else:
            return True

    return False


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])

    top, bot = 0, m - 1
    while top <= bot:
        row = (top + bot) // 2

        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if top > bot:
        return False

    row = (top + bot) // 2
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2

        if matrix[row][mid] < target:
            l = mid + 1
        elif matrix[row][mid] > target:
            r = mid - 1
        else:
            return True

    return False


if __name__ == "__main__":
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert not searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
