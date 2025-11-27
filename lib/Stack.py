# lib/Stack.py

class Stack:
    def __init__(self, items=None, limit=100):
        """Initialize a stack with optional items and a limit."""
        if items is None:
            self.items = []
        else:
            if len(items) > limit:
                raise ValueError("Initial items exceed stack limit")
            self.items = items
        self.limit = limit

    def isEmpty(self):
        """Return True if stack is empty, False otherwise."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack if not full."""
        if not self.full():
            self.items.append(item)

    def pop(self):
        """Remove and return the top item. Returns None if empty."""
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        """Return the top item without removing it."""
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

    def full(self):
        """Return True if the stack is at its limit."""
        return len(self.items) >= self.limit

    def search(self, target):
        """Return distance from top to target (0 if top, -1 if not found)."""
        try:
            # distance from top = number of elements above target
            return len(self.items) - 1 - self.items.index(target)
        except ValueError:
            return -1
