class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.count:
            temp_num = self.num
            self.num += self.step
            self.i += 1
            return temp_num
        raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
