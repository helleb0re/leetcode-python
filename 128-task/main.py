from typing import List


def longestConsecutive(nums: List[int]) -> int:
    store = set(nums)

    best_res = 0
    for num in store:
        # this is the key for O(n) solution
        # check if its the start of a sequence
        if not num - 1 in store:
            res = 1
            next_consecutive_num = num + 1
            # think of it like a store.remove(next_consecutive_num + 1)
            # if next_consecutive_num + 1 in the store
            while next_consecutive_num in store:
                next_consecutive_num += 1
                res += 1

            if res > best_res:
                best_res = res

    return best_res


if __name__ == "__main__":
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert (
        longestConsecutive([1, -8, 7, -2, -4, -4, 6, 3, -4, 0, -7, -1, 5, 1, -9, -3])
        == 6
    )
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1]) == 1
