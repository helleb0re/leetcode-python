import math
from typing import List


# neetcode solution
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2

        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / k)  # upper rounding

        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res


# another solution with the editing "standard" binary search
def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)

    while l < r:
        k = (l + r) // 2

        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / k)  # upper rounding

        if hours <= h:
            r = k
        else:
            l = k + 1

    return l


if __name__ == "__main__":
    assert minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
