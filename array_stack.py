class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def __is_empty__(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)
    def top(self):
        if self.__is_empty__():
            raise Empty('Stack empty.')
        return self._data[-1]
    def pop(self):
        if self.__is_empty__():
            raise Empty('Stack empty.')
        self._data.pop()

if __name__ == '__main__':
    new = ArrayStack()
    new.push(4)
    new.push(6)
    print(new.pop())
    print(new.top())
    print(new.__len__())
    print(new._data)
