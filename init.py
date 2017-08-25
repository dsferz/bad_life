import animals


class A:
    testval = 100
    def __init__(self, age = 50):
        self.age = age

class B(A):
    testval = 200
    def __init__(self, value):
        A()
        self.testval = value

if __name__ == '__main__':
    test = B(50)
    test.testval -= 50
    print test.age
    