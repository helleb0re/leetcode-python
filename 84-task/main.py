from typing import List


# main idea is to use the monotonic stack,
# which contains `pair(value, index)` in non-decreasing order
# and pop elements if they > then current element in `heights`
# (they are boundaries)
def largestRectangleArea(heights: List[int]) -> int:
    buffer = []  # stack: pair(value, index)
    max_area, n = 0, len(heights)
    for i in range(n):
        push_index_buff_elem = i
        while buffer and buffer[-1][0] > heights[i]:
            buff_elem, buff_elem_index = buffer.pop()
            push_index_buff_elem = buff_elem_index
            max_area = max(max_area, buff_elem * (i - buff_elem_index))
        buffer.append((heights[i], push_index_buff_elem))

    while buffer:
        buff_elem, buff_elem_index = buffer.pop()
        max_area = max(max_area, buff_elem * (n - buff_elem_index))

    return max_area


if __name__ == "__main__":
    assert largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert largestRectangleArea([2, 4]) == 4
