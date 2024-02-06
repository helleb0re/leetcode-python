from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    store = dict()
    max_freq = 0
    for num in nums:
        store[num] = store.setdefault(num, 0) + 1
        if store[num] > max_freq:
            max_freq = store[num]

    # bucket sort of number's frequencies
    bucket = [[] for _ in range(max_freq + 1)]
    for num, freq in store.items():
        bucket[freq].append(num)

    res = []
    for elems in reversed(bucket):
        for elem in elems:
            res.append(elem)
            if len(res) == k:
                return res


if __name__ == "__main__":
    assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert topKFrequent([1], 1) == [1]
