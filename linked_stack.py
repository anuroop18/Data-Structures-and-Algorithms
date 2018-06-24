class Empty(Exception):
    pass

class LinkedStack:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  #initiaalize node's fields
            self._element = element  #reference to users elements
            self._next = next  #reference to next node

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer



if __name__ == '__main__':
    data = [1,2,3,4]
    S = LinkedStack()
    S.push(data)
    S.push([1,3,5,6,7,3])
    S.push(1)
    S.push('aaaaaaaaaaa')
    print(len(S))
    print(S.top())
    print(S.is_empty())
