class Example:
    class_var = "Class Variable"

    def __init__(self, value):
        self.instance_var = value

    def instance_method(self):
        return f"Instance Variable: {self.instance_var}"

    @classmethod
    def class_method(cls):
        return f"Class Variable: {cls.class_var}"

    @staticmethod
    def static_method():
        return "Static Method - No access to instance or class variables"

obj = Example("Test")
print(obj.instance_method())  # Output: Instance Variable: Test
print(Example.class_method())  # Output: Class Variable: Class Variable
print(Example.static_method())  # Output: Static Method - No access to instance or class variables