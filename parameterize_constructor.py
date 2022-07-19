"""
parameterized constructor là khởi tạo có tham số. Khi có tham số thực hiện khởi tạo parameter.

"""

class animal:
    legs = 0
    # Parameterized Constructor
    def __init__(self, legs):
        self.legs_num = legs

    def print_legs(self):
        print(self.legs_num)

# Khởi tạo đối tượng "dog" của class "Animal"
# Parameterized constructor cần phải truyền thông số vào
dog = animal(4)
print(dog.legs_num) # print attribute in __init__ of class
dog.print_legs() # call function in class