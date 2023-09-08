
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("halo nama sy adlh " + self.name)

p1=Person("John", 36)
p1.myfunc()