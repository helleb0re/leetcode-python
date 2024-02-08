from typing import List
from collections import deque


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)

    res = [1]
    for i in range(n - 1):
        res.append(nums[i] * res[i])

    suff_prod = 1
    for i in range(n - 1, 0, -1):
        suff_prod *= nums[i]
        res[i - 1] *= suff_prod

    return res


if __name__ == "__main__":
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
