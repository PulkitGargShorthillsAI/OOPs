
class PyCharm:

    def execute(self):
        print("compliling")
        print("execute")

class MyEditor:

    def execute(self):
        print("spell check")
        print("compliling")
        print("execute")

class A:

    def run(self,ide):
        ide.execute()

a1 = A()
ide1 = PyCharm()
ide2 = MyEditor()

a1.run(ide1)
print()
a1.run(ide2)