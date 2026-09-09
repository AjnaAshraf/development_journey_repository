class Father:

    def cricket_skills(self):

        print("I am good at cricket ")

    def dancing_skills(self):

        print("I am good at dancing ")

class Mother:

    def dancing_skills(self):

        print("I am good at dancing")

class Child(Father,Mother):

    def coding_skills(self):

        print("I am good at coding")


child_inst = Child()

child_inst.coding_skills()
child_inst.dancing_skills()
child_inst.cricket_skills()