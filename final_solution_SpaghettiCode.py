class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.takenCourses = []
        self.chosenCourseIndex = 0
        self.minValue = 3
        self.maxValue = 5
        
    def welcomeStudent(self):
        print("Hello", self.name)
        
    def checkStudent(self):
        chanse = 3     
        while True:
            if(chanse != 0):
                name = input("Type your name : ")
                surname = input("Type your surname : ")
                if(self.name == name and self.surname == surname):
                    print("---Login successful---")
                    self.welcomeStudent()
                    break
                elif name == "" or surname == "":
                    chanse-=1
                    print("Please fill in the blanks : ")
                else:
                    chanse-=1
            else:
                print("Please try again later")
                exit()
                                          
    def takeCourses(self):
        course1 = Course()
        course1.addCourse()
        print(f"You can take a minimum of {self.minValue} and a maximum of {self.maxValue} lessons")
        i = 1
        print("Exit to press 'q'")
        while(True):
            if (i <= self.maxValue):
                course1.showCourses()
                num = input("Choose course : ")
                self.takenCourses.append(course1.courses[int(num)-1])
                if(i >=3 and str(num) == "q"):
                    exit()
                i+=1
            else:
                break
        course1.showCourses()
        self.chosenCourseIndex = int(input("Choose course to exam : "))
        exam1 = Exam()
        exam1.takeExam()
        

class Exam():
    def __init__(self):
        self.midterm = 0
        self.final = 0
        self.project = 0
        self.exam = {}
        
    def takeExam(self):
        self.midterm = int(input("Enter midterm: "))
        self.final = int(input("Enter final : "))
        self.project = int(input("Enter project : "))
        self.exam["midterm"] = self.midterm
        self.exam["final"] = self.final
        self.exam["project"] = self.project
        grade1 = Grade(self.exam)
        grade1.calculateGrade()

class Course():
    def __init__(self, courseCount = 5):
        self.courses = []
        self.courseCount = courseCount
        
    def addCourse(self):
        print("---Enter 5 course names...--- \n")
        for i in range(0,self.courseCount):
            course = input("Enter {}. course name : ".format(i+1))
            self.courses.append(course)
            
    def showCourses(self):
        print("\nCourse List : ")
        for i in range(0,len(self.courses)):
            print(f"\t[{i+1}]",self.courses[i])
            
class Grade():
    def __init__(self, exam):
        self.exam = exam
        self.grade = ""

    def calculateGrade(self):
        return self.checkGrade(self.exam["midterm"] * 0.3 + self.exam["final"] * 0.5 + self.exam["project"] * 0.2)

    def checkGrade(self,grade):
        if grade > 90:
            self.grade = "AA"
        elif 70 <= grade < 90:
            self.grade = "BB"
        elif 50 <= grade < 70:
            self.grade = "BB"
        elif 30 <= grade < 50:
            self.grade = "BB"
        elif grade < 30:
            self.grade = "FF"
            print("You failed! Study hard!")
        self.showGrade()
    def showGrade(self):
        print(self.grade)
            
def main():
    student1 = Student("ben","sen")
    student1.checkStudent()
    student1.takeCourses()

main()
        
