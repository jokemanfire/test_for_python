class Student(object):
    def __init__(self,name = "hu", score = "100"):
        self.__name = name
        self.__score = score

    def print_score(self,*args):
        print("%s is %s"%(self.__name,self.__score))
        if args is not None:
            for i in range(len(args)):
                print("%s"%str(args[i]))

    def chang_score(self, price):
        self.__price = price

class Little_student(Student):
    def test():
        return None

student = Little_student()
#student.print_score("location is sichuan", "hubaba")
print(dir(student))
