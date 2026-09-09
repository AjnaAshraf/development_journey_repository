"""
object oriented programming --- it is a way of programing to convert a real world object to program using class and objects

class - plan ,design pattern, template,blueprint for creating real world object

objects - real world entities ,built using class

class Class_name:

    attribute:type
    attribute:type
    attribute:type
    .............


    def method_name(self)
        method definition 
    def method_name(self)
        method definition 
    def method_name(self)
        method definition 


"""

class Animal:

    name:str

    sound:str

    def walk(self):

        print("animal is walking")

    def sleep(self):

        print("animal is sleeping")

cat = Animal()
dog = Animal()

dog.walk()
cat.sleep()