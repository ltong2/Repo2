class Student:
    courseMarks={}
    name= ""
    family= ""
    def __init__(self, name, family):
        self.name=name
        self.family=family
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        print("%s, this course is being added " %course)
    def average(self):
        total=0
        for i in self.courseMarks.keys():
            #print (i)
            total=total+self.courseMarks[i]
            avg=total/len(self.courseMarks)
        print("the average is %d for %s %s" %(avg,self.name, self.family))
            
def main():
    newStudent = Student("jeff", "ye")
    newStudent.addCourseMark("CMPUT410",40)
    newStudent.addCourseMark("CMPUT310",50)
    newStudent.addCourseMark("CMPUT30",50)
    newStudent.average()

    newStudent = Student("frank", "gg")
    newStudent.addCourseMark("CMPUT410",90)
    newStudent.addCourseMark("CMPUT310",50)
    newStudent.addCourseMark("CMPUT320",50)
    newStudent.average()
    newStudent = Student("dog", "ye")
    newStudent.addCourseMark("CMPUT410",90)
    newStudent.addCourseMark("CMPUT310",90)
    newStudent.average()
    newStudent = Student("sb", "john")
    newStudent.addCourseMark("CMPUT410",10)
    newStudent.addCourseMark("CMPUT310",50)
    newStudent.addCourseMark("CMPUT110",50)
    newStudent.average()

main()
