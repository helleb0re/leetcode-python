from typing import List


# []
# [1], [1, 2], [1, 2, 3]
# [2], [2, 3]
# [3]

# my approach to solve this problem

## [1, 2]

### [1, 3]
## [1, 2, 3]

#### [1, 4]
### [1, 3, 4]
## [1, 2, 4]
## [1, 2, 3, 4]

##### [1, 5]
#### [1, 4, 5]
### [1, 3, 5]
### [1, 3, 4, 5]
## [1, 2, 5]
## [1, 2, 3, 5]
## [1, 2, 4, 5]
## [1, 2, 3, 4, 5]


# my solution
def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]
    for i in range(len(nums)):
        result.append([nums[i]])

        stack = []
        for j in range(i + 1, len(nums)):

            for k in range(len(stack) - 1, -1, -1):
                stack.append(stack[k] + [nums[j]])

            stack.append([nums[i], nums[j]])

        result.extend(stack)

    return result


from collections import deque


# neetcode solution (iteration) O(n * 2^n)
def subsets(nums: List[int]) -> List[List[int]]:
    result = deque([[]])

    for i in range(len(nums)):
        for _ in range(len(result)):
            elem = result.popleft()
            # we always have two choices:
            # 1. add [curr_num]
            result.append(elem + [nums[i]])
            # 2. add []
            result.append(elem + [])

    return result


if __name__ == "__main__":
    assert sorted(subsets([1, 2, 3])) == sorted(
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert sorted(subsets([0])) == sorted([[], [0]])
