from problem1 import containsDuplicate

def test():
    print(containsDuplicate([1, 2, 3, -1]))  # False
    print(containsDuplicate([1, 2, -3, 4]))  # False
    print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
    print(containsDuplicate([0, 0, 0, 1]))  # True
test()