# Tính đa hình có 3 loại:
# Đa hình với các class method

'''class Dog:
    def age(self):
        print("Age: ", 9)
    def name(self):
        print("Name: Kiki")

class chicks:
    def age(self):
        print("Age: ", 1)
    def name(self):
        print("Name: Yolo")

cho = Dog()
ga = chicks()

cho.age()
cho.name()

ga.age()
ga.name()

print()'''
# Đa hình với các inheritance

class Animal:
    def age(self):
        print("Age:", 10)
    def name(self):
        print("Name: Kiki")

class dog(Animal):
    def name(self):
        print("Name: Gau gau")
class chick(Animal):
    def age(self):
        print("Age: ", 1)

dongvat = Animal()
cho = dog()
ga = chick()

cho.age()
cho.name()
ga.age()
ga.name()