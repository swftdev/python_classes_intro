class Student:
    def __init__(self, name, gradeLevel):
        self.name = name
        self.gradeLevel = gradeLevel
        self.graduated = True if gradeLevel > 12 else False

    @classmethod
    def fromDict(cls, studentDict):
        return cls(studentDict["name"], studentDict["gradeLevel"])

    @staticmethod
    def isGraduated(student):
        return student.graduated


justin = Student("Justin", 13)
adam = Student.fromDict({
    "name": "Adam",
    "gradeLevel": 11
})

print(justin, adam)
print(Student.isGraduated(justin))
print(Student.isGraduated(adam))