class Student:
    def __init__(self,name:str,age:int, city:str):
        self.name = name
        self.age = age
        self.city = city

    # def set_info(self):
    #     self.name=input("Enter Your name")
    #     self.age= int(input('Enter your age'))
    #     self.city=input("Enter your City")

    # def set_info(self, name: str, age: int, city: str):
    #     self.name = name
    #     self.age = int(age)
    #     self.city = city

    def display(self) -> None:
        print(f'this is a display func {self.name},{self.age},{self.city}')


s1 = Student("pintu",10, 'kota')

# s1.name="pintu"
# s1.age=10
# s1.city="pintukota"

# print(s1.name,s1.age, s1.city, end=' ')

# good way
# s1.set_info("pintu",10,"kota")
s1.display()
