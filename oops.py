# classes and objects
class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is: ',self.cpu,self.ram)


comp1 = Computer('i5','16gb')
comp2 = Computer('i7','32gb')
comp1.config()
comp2.config()





