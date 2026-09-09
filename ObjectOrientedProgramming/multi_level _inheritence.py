class GrandParent:

    def properties(self):

        print("2 acre land ")

class Parent(GrandParent):

    def home(self):

        print("15000 sqft house")

class Child(Parent):

    def social_media_accnt(self):

        print("child has a instagram account")


child_inst = Child()

child_inst.social_media_accnt()
child_inst.home()
child_inst.properties()