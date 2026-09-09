"""
child class can access the methods and properties of parent class=> inheritence

"""

class Parent:

    def house(self):

        print("parent owns house")


class Child(Parent):

    def social_media_account(self):

        print("child has social media account")


Child_instance = Child()
Child_instance.social_media_account()
Child_instance.house()