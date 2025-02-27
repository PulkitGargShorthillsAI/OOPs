class Car:

    wheels = 4

    def __init__(self):
        self.name = "BMW"
        self.mil = 18

c1 = Car()
c2 = Car()

Car.wheels = 5

print(c1.mil,c1.name,c1.wheels)
print(c2.mil,c2.name,c2.wheels)