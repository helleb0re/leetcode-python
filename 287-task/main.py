from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow, fast = nums[0], nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    second_slow = nums[0]
    while second_slow != slow:
        second_slow = nums[second_slow]
        slow = nums[slow]

    return slow


if __name__ == "__main__":
    # assert findDuplicate([1, 3, 4, 2, 2]) == 2
    # assert findDuplicate([3, 1, 3, 4, 2]) == 3
    # assert findDuplicate([3, 3, 3, 3, 3]) == 3
    assert findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) == 9
