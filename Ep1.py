#Làm quen với OOP
class info:
    stt = 1
    hanh_kiem = "Tốt"
    def __init__(self, paraName, paraAge, paraGender):
        self.name = "Hoc sinh " + paraName
        self.age = paraAge
        self.gender = paraGender
    def hello(self):
        return "Xin chao " + self.name
    @classmethod #Sử dụng phương thức classmethod để thay đổi giá trị biến của toàn bộ class
    def hanh_kiem_Update(cls, hk): #Có thể thay đổi cls = self, nhưng ngta vẫn quen dùng self
        cls.hanh_kiem = hk


code36 = info("Kien", "18", "Nam")

print(code36.name)
print("Tuoi:", code36.age)
print("Gioi tinh:", code36.gender)

print(info.hello(code36)) #Cách phức tạp
print(code36.hello()) #Cách phổ biến, ngắn gọn

code36.hanh_kiem_Update("Khá") #Cập nhật giá trị biến
print("Hanh kiem:", code36.hanh_kiem)