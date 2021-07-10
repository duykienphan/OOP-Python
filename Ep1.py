class info:
    def __init__(self, paraTen, paraAge, paraGender):
        self.ten = "Hoc sinh " + paraTen
        self.age = paraAge
        self.gender = paraGender
    def hello(self):
        return "Xin chao " + self.ten

code36 = info("Kien", "18", "Nam")
print(code36.ten)
print("Tuoi:", code36.age)
print("Gioi tinh:", code36.gender)

print(info.hello(code36))