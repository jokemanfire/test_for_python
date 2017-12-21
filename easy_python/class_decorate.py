class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        self.__score = value
    @property
    def test(self):
        return self.__com
    @test.setter
    def test(self, com):
        self.__com = com

student = Student()
student.score = 22
print(student.score)
student.test = "no"
print (student.test)
