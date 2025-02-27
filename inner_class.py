class Student:

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = Student.Laptop()

    def show(self):
        print(self.name,self.roll_no)

    class Laptop:
        def __init__(self):
            self.name = "hp"
            self.cpu = 'i5'
            self.ram = '16gb'

        def show(self):
            print(self.name,self.cpu,self.ram)


s1 = Student('Ram',2)
s2 = Student('Sham',3)

s1.show()
s1.lap.show()

s2.show()
s2.lap.show()