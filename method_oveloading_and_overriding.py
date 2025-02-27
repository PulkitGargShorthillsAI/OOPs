class A:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def show(self):
        print("in A")
        
    def add(self,a=None,b=None,c=None):
        s = 0

        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        elif a != None:
            s = a
        return s
    
class B(A):

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def show(self):
        print("In B")
        

a1 = A(3,4)

print(a1.add())

b1 = B(2,3)
b1.show()