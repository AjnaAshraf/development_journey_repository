"""
method_overriding => child class redefines the method that is already defined in the parent class

"""

class Parent:

    def mobile(self):

        print("Redmi note pro")

class Child(Parent):

    def mobile(self):

        print("one plus nord")

child_instance = Child()
child_instance.mobile()
