class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index_i = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_i >= 0:
            temp = self.iterable[self.index_i]
            self.index_i -= 1
            return temp
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
