from typing import List


class Queue():
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items: List[int] = []

    def is_empty(self) -> bool:
        return not self.items

    def is_full(self) -> bool:
        return len(self.items) == self.capacity

    def dequeue(self) -> int:
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.items.pop(0)

    def enqueue(self, item: int) -> None:
        if self.is_full():
            raise ValueError("Queue is full")
        self.items.append(item)

    def front(self) -> int:
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.items[0]


if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    
    print(queue.is_full())
    print(queue.front())
    print(queue.dequeue())
    print(queue.front())
    print(queue.dequeue())
    print(queue.is_empty())

