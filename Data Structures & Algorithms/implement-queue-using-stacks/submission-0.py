class MyQueue:

    def __init__(self):
        self.in_stack = []    # new elements are pushed here
        self.out_stack = []   # elements are popped/peeked from here (front of queue on top)

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self) -> None:
        # Refill out_stack only when it's empty. Popping everything from
        # in_stack reverses the order, so the oldest element ends up on top.
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())