
class A:
    def __init__(self):
        print('in A')

    def feature1(self):
        print('Working on fetaure 1')

    def feature2(self):
        print('Working on fetaure 2')

class B(A):
    def __init__(self):
        print('in B')

    def feature3(self):
        print('Working on fetaure 3')

    def feature4(self):
        print('Working on fetaure 4')

class C:
    def feature5(self):
        print("Working on feature 5")

class D(A,C):
    def __init__(self):
        super().__init__()
        print('in D')

b1 = B()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

d1 = D()
d1.feature1()
d1.feature2()
d1.feature5()