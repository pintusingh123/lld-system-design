class Teacher:
    def __init__(self, name: str) -> None:
        self.__name: str = name

    def get_name(self) -> str:
        return self.__name

    def teach(self, std: "Student") -> None:
        print(f"{self.__name} is teaching {std.get_name()}")


class Student:
    def __init__(self, name: str) -> None:
        self.__name: str = name

    def get_name(self) -> str:
        return self.__name


Teacher1 = Teacher("pintu")
std1 = Student("rahul")

Teacher1.teach(std1)
 