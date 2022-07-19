"""
Là quá trình xây dựng một class (class con) từ một class đã được khai báo từ trước (class cha). 
Class con có thể tái sử dụng, overwrite hay extend các attribute và method của class cha mà không cần khai báo lại

"""

class animal:
    # contructor
    def __init__(self, id, legs):
        # Khởi tạo attribute (thuộc tính)
        self.id = id
        self.legs = legs

    def get_info(self):
        print(self.id)
        print(self.legs)
    
    def checkDog(self):
        return False

# Thực hiện kế thừa từ class Animal
# class Animal là cha, class Dog là con
class Dog(animal):
    # Constructor
    def __init__(self, id, legs):
        # super().__init__(2, 5)      [1]
        animal.__init__(self, id, legs)
        # Khởi tạo thông số cho class Dog
        self.id = 10
        self.legs = 4
    # Overwrite method checkDog, vì class con có thể truy cập vào class cha theo đúng nguyên lý OOP
    def checkDog(self):
        return True
    # Ngoài overwrite ra, class con có thể định nghĩa 1 method mới 
    def checkCat(self):
        return False

cho = Dog(5, 2)
print(cho.checkDog())
print(cho.checkCat())
