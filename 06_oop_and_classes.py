class Students:
    count = 0
    gpa_total = 0

    def __init__(self, name, gpa: float):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.gpa_total += gpa

    def get_info(self):
        print(f"{self.name} = {self.gpa:.2f}")

    @classmethod
    def get_average(cls):
        print(f"Average gpa: {Students.gpa_total / cls.count:.2f}")
        print(f"Count: {cls.count}")


student1 = Students("Kiran", 8.19)
student2 = Students("Mahesh", 8.6)
student3 = Students("Pavan", 8.9)
Students.get_average()

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

my_dog = Dog()
my_dog.speak()

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width

r = Rectangle(3, 4)
r.width = 5
print(r.width)
