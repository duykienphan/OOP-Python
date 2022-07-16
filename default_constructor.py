"""
Default constructor là khởi tạo không có parameter

"""

class animal:
    # Default Constructor
    def __init__(self): #Thuộc tính trong class
        self.legs = 4
    
    def print_legs(self): #Hàm trong class
        print(self.legs)

# Khởi tạo đối tượng "dog" của class "animal"
dog = animal()
print(dog.legs)
dog.print_legs()