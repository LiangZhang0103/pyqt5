
class A:

    def __init__(self, x=10, y=10):
        self.x = x
        self.y = y 

    def foo(self):
        pass
    

class B(A):

    # def __init__(self, x, y, z):
    #     super().__init__(x)
    #     self.z = z 

    def foo(self):
        print('a')

# b = B(10, 10, 100)

b = B(10, 20)
print(b.x)
print(b.y)