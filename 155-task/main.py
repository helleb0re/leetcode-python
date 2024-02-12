class MinStack:
    def __init__(self):
        self.store = []
        self.min_store = []

    def push(self, val: int) -> None:
        self.store.append(val)

        min_value = val
        if len(self.min_store) != 0 and self.min_store[-1] < val:
            min_value = self.min_store[-1]

        self.min_store.append(min_value)

    def pop(self) -> None:
        self.store.pop()
        self.min_store.pop()

    def top(self) -> int:
        return self.store[-1]

    def getMin(self) -> int:
        return self.min_store[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()
