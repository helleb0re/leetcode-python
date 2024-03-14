from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    return -1


if __name__ == "__main__":
    # assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    # assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([-1, 0, 3, 5, 9, 12], 5) == 5
