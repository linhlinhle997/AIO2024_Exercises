from typing import List


class Stack():
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items: List[int] = []

    def is_empty(self) -> bool:
        return not self.items

    def is_full(self) -> bool:
        return len(self.items) == self.capacity

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()

    def push(self, item: int) -> None:
        if self.is_full():
            raise ValueError("Stack is full")
        self.items.append(item)

    def top(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.items[-1]


if __name__ == "__main__":
    stack = Stack(10)
    stack.push(1)
    stack.push(2)

    print(stack.is_full())
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(stack.is_empty())
