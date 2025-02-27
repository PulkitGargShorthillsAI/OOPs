class Student:

    roll_no = 1
    def __init__(self):
        self.name = "Pulkit"
        self.roll_no = Student.roll_no
        Student.roll_no += 1

    def update_detals(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no


    def show_detals(self):
        print(f'{self.name}  {self.roll_no}')

    def compare(self,s1):
        if self.name == s1.name:
            print("Students have same name")
        else:
            print("Students have different name")


s1 = Student()
s2 = Student()
s1.show_detals()
s2.show_detals()

s1.compare(s2)