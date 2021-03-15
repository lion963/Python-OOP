from collections import deque


class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.keys = deque(self.dict_object.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys:
            key = self.keys.popleft()
            value = self.dict_object[key]
            return key, value
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
