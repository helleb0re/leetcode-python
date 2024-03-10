from collections import deque


# this approach use the monotonically decreasing queue


# my solution
def maxSlidingWindow(nums, k):
    l = 0
    buff = deque()
    for i in range(l, k):
        while buff and buff[-1] < nums[i]:
            buff.pop()
        buff.append(nums[i])

    res = [buff[0]]
    for r in range(k, len(nums)):
        while buff and buff[-1] < nums[r]:
            buff.pop()
        buff.append(nums[r])

        if buff[0] == nums[l]:
            buff.popleft()

        res.append(buff[0])
        l += 1

    return res


# neetcode solution
def maxSlidingWindow(nums, k):
    l = 0
    buff = deque()

    res = []
    for r in range(len(nums)):
        while buff and nums[buff[-1]] < nums[r]:
            buff.pop()
        buff.append(r)

        if l > buff[0]:
            buff.popleft()

        if r + 1 >= k:
            res.append(nums[buff[0]])
            l += 1

    return res


if __name__ == "__main__":
    assert maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert maxSlidingWindow([1], 1) == [1]
    assert maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]
