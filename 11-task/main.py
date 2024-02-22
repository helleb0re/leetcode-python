from typing import List


def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_size = 0
    while l < r:
        local_size = min(height[l], height[r]) * (r - l)
        max_size = max(max_size, local_size)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_size


if __name__ == "__main__":
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1
