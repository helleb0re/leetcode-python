from typing import List


# solution with O(2*n) => O(n) memory
# and O(n) time
def trap(height: List[int]) -> int:
    right_max_heights, left_max_heights = [], []
    right_max_height, left_max_height = -1, -1
    k1, k2 = 1, 1
    n = len(height)
    for i in range(len(height)):
        if left_max_height < height[i]:
            if left_max_height != -1:
                left_max_heights += [left_max_height] * k1
            left_max_height = height[i]
            k1 = 0

        if right_max_height < height[n - i - 1]:
            if right_max_height != -1:
                right_max_heights = [right_max_height] * k2 + right_max_heights
            right_max_height = height[n - i - 1]
            k2 = 0

        k1 += 1
        k2 += 1

    left_max_heights += [left_max_height] * k1
    right_max_heights = [right_max_height] * k2 + right_max_heights

    water = 0
    for i, h in enumerate(height):
        water += min(left_max_heights[i], right_max_heights[i]) - h

    return water


# solution with O(n) memory and O(n) time
# check explanation
def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_left, max_right = height[l], height[r]
    water = 0
    while l < r:
        if max_left <= max_right:
            l += 1
            add_water = min(max_left, max_right) - height[l]
            max_left = max(max_left, height[l])
        else:
            r -= 1
            add_water = min(max_left, max_right) - height[r]
            max_right = max(max_right, height[r])

        water += max(add_water, 0)

    return water


if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
