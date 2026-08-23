class Student:

    def __init__(self, name):
        self.name = name

    # Normal method
    def show_name(self):
        print(self.name)

    # Static method
    @staticmethod
    def add(a, b):
        return a + b
student = Student("laoxiang")
student.show_name()
print(Student.add(11,11))