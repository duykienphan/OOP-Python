# Có 2 loại kế thừa: Kế thừa đơn và đa kế thừa
# Kế thừa đơn example: inheritance.py
# Thực hiện đa kế thừa khi 1 class con có kế thừa từ 2 class cha trở lên như ví dụ bên dưới.

class Dad:
    fatherName = ""

    def __init__(self, fatherName):
        self.fatherName = fatherName

    def returnName(self):
        print(self.fatherName)

class Mom:
    motherName = ""
    def returnName(self):
        print(self.motherName)

# Thực hiện kế thừa 2 class, class Son có thể kế thừa được 2 class cha bao gồm: class Dad và class Mom
class Son(Dad, Mom):
    def parentsName(self):
        print(self.fatherName)
        print(self.motherName)

dad = Dad("kien")
dad.returnName()
