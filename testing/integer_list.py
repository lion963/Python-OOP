class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):

    def setUp(self):
        self.integer_list = IntegerList(2, 4, 5, 6, 'as')

    def test_constructor_and_get_data_method(self):
        result = self.integer_list.get_data()
        expected_result = [2, 4, 5, 6]
        self.assertEqual(result, expected_result)

    def test_add_method_integer(self):
        result = self.integer_list.add(8)
        expected_result = [2, 4, 5, 6, 8]
        self.assertEqual(result, expected_result)

    def test_add_method_not_integer_raise_error(self):
        with self.assertRaises(ValueError):
            self.integer_list.add('not integer')

    def test_remove_index_method_valid_index(self):
        result = self.integer_list.remove_index(3)
        expected_result = 6
        self.assertEqual(result, expected_result)

    def test_remove_index_method_not_valid_index_raise_error(self):
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(4)

    def test_get_method_valid_index(self):
        result = self.integer_list.get(1)
        expected_result = 4
        self.assertEqual(result, expected_result)

    def test_get_method_not_valid_index_raise_error(self):
        with self.assertRaises(IndexError):
            self.integer_list.get(5)

    def test_insert_method_valid_index(self):
        self.integer_list.insert(0, 1)
        result = self.integer_list.get_data()
        expected_result = [1, 2, 4, 5, 6]
        self.assertEqual(result, expected_result)

    def test_insert_method_not_valid_index_raise_error(self):
        with self.assertRaises(IndexError):
            self.integer_list.insert(4, 6)

    def test_insert_method_not_integer_index_raise_error(self):
        with self.assertRaises(ValueError):
            self.integer_list.insert(3, 'not integer')

    def test_get_biggest_method(self):
        result = self.integer_list.get_biggest()
        expected_result = 6
        self.assertEqual(result, expected_result)

    def test_get_index_method(self):
        result = self.integer_list.get_index(4)
        expected_result = 1
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
