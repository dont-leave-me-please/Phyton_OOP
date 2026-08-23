class Teacher:

    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching")


class Department:

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
    
    def show_teacher(self):
        print(f"{self.teacher.name} works in {self.name}") #self.teacher.name the name comes from the Teacher class in our example.


teacher1 = Teacher("Dara")

department1 = Department("Computer Science", teacher1)


#department1
#    │
#    ├── name = "Computer Science"
#    │
#    └── teacher ─────→ teacher1
#                         │
#                         └── name = "Dara"#


department1.show_teacher()
teacher1.teach()