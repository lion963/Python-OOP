class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string) - 1:
            raise StopIteration()

        self.index += 1
        if self.string[self.index] in self.vowels:
            return self.string[self.index]
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
