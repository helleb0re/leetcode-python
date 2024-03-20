import math


def bisect(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] > target:
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            return m

    return math.floor((l + r) / 2)


class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        key_arr = self.store[key]

        idx = self.__bisect(key_arr, timestamp)

        if idx < 0:
            return ""

        return key_arr[idx][1]

    def __bisect(self, arr, target):
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m][0] > target:
                r = m - 1
            elif arr[m][0] < target:
                l = m + 1
            else:
                return m

        return math.floor((l + r) / 2)


if __name__ == "__main__":
    # arr = [0, 1, 3, 4, 5]
    # target = 2
    # idx = bisect(arr, target)
    # print(idx)

    # timeMap = TimeMap()
    # timeMap.set("foo", "bar", 1)
    # timeMap.get("foo", 1)
    # timeMap.get("foo", 3)
    # timeMap.set("foo", "bar2", 4)
    # timeMap.get("foo", 4)
    # timeMap.get("foo", 5)

    timeMap = TimeMap()
    timeMap.set("love", "high", 10)
    timeMap.set("love", "low", 20)
    print(timeMap.get("love", 5))
    print(timeMap.get("love", 10))
    print(timeMap.get("love", 15))
    print(timeMap.get("love", 20))
    print(timeMap.get("love", 25))
