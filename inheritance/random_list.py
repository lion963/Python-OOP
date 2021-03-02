import random

class RandomList(list):

    def get_random_element(self):
        element=random.choice(self)
        self.remove(element)
        return element


l=[2,3,4,5]
random_l=RandomList(l)
print(random_l)
print(random_l.get_random_element())
print(random_l)
