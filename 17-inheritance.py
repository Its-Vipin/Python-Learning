class A:
    def __init__(self):
        print("a")
    def method1(self):
        print("This is method 1")

    def method2(self):
        print("This is method 2")

class B(A):
    def __init__(self):
        super().__init__()
        print("b")
    def method3(self):
        print("This is method 3")

    def method4(self):
        print("This is method 4")

obj = B()