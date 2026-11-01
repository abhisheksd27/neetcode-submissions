from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self._top = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self._top = x

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self._top = self.q.popleft()   # last element moved becomes the new top
            self.q.append(self._top)
        return self.q.popleft()

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return not self.q