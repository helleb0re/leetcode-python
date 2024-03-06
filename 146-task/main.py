# my solution
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.dummy = ListNode()
        self.tail = self.dummy

        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val, node = self.cache[key]
        if node != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            _, node = self.cache[key]
            self.cache[key] = [value, node]
            _ = self.get(key)
        else:
            node = ListNode(key, prev=self.tail)

            self.cache[key] = [value, node]
            self.tail.next = node
            self.tail = self.tail.next

            if len(self.cache) > self.capacity:
                del self.cache[self.dummy.next.val]
                self.dummy.next = self.dummy.next.next
                self.dummy.next.prev = self.dummy


def first_test():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


def second_test():
    cache = LRUCache(1)
    cache.put(2, 1)
    print(cache.get(2))
    cache.put(3, 2)
    print(cache.get(2))
    print(cache.get(3))


def third_test():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    print(cache.get(2))
    cache.put(1, 1)
    cache.put(4, 1)
    print(cache.get(2))


def fourth_test():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
    print(cache.get(2))


if __name__ == "__main__":
    # first_test()
    # print("-" * 10)
    second_test()
    print("-" * 10)
    third_test()
    print("-" * 10)
    fourth_test()
