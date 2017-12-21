class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if value <= 60:
            raise ValueError("rubbish")
        self.__score = value
    def test(self):
        print("no")
        return self.test
    def __str__(self):
        return "none"
student = Student()
#student.score = 60
#student.score = 80
#x = student.test()
#print(x)
print(Student())
