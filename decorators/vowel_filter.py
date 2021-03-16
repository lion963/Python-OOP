def vowel_filter(function):
    def wrapper():
        letters = function()
        result = [letter for letter in letters if letter in 'aeiou']
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
