from typing import List


# my solution (neetcode explanation)
def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    res = nums[0]

    while l <= r:
        m = (l + r) // 2
        res = min(res, nums[m])

        if nums[m] >= nums[0]:
            l = m + 1
        else:
            r = m - 1

    return res


# neetcode solution
def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    res = nums[0]

    while l <= r:
        # if array (or part of array) is already sorted
        # then we need to return the first element
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        # else we need to move our pointers (l or r)
        m = (l + r) // 2
        res = min(res, nums[m])
        # if we stay on the left part of array
        # then we need to move left pointer to the middle
        if nums[m] >= nums[l]:
            l = m + 1
        # else we need to move right pointer to the middle
        else:
            r = m - 1

    return res


if __name__ == "__main__":
    assert findMin([3, 4, 5, 1, 2]) == 1
    assert findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert findMin([11, 13, 15, 17]) == 11
    assert findMin([2, 1]) == 1
