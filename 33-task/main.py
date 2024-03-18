from typing import List


# my solution
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    pivot = l

    while l <= r:
        m = (l + r) // 2

        if nums[m] < nums[0]:
            pivot = m
            r = m - 1
        else:
            l = m + 1

    if pivot == 0 or nums[0] > target:
        l, r = pivot, len(nums) - 1
    else:
        l, r = 0, pivot - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    return -1


# neetcode solution
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if nums[m] < target or nums[l] > target:
                l = m + 1
            else:
                r = m - 1
        else:
            if nums[m] > target or nums[r] < target:
                r = m - 1
            else:
                l = m + 1

    return -1


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 6) == 2
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([1, 3], 3) == 1
    assert search([3, 1], 1) == 1
    assert search([5, 1, 3], 5) == 0
    assert search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
