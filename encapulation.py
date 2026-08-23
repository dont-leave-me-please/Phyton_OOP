class Student:

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):

        if 0 <= score <= 100:
            self.__score = score
        else:
            print("Invalid score")
student = Student("Dara", 80)
print(f"The student's name is {student.name} and the score is {student.get_score()}")
student.set_score(90)
print(f"The student's name is {student.name} and the score is {student.get_score()}")
student.set_score(150)
print(f"The student's name is {student.name} and the score is {student.get_score()}")