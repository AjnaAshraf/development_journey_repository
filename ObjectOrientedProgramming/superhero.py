class Superhero():

    name:str
    power:str
    universe:str

    def set_superhero(self,name,power,universe):

        self.name=name
        self.power=power
        self.universe=universe

    def get_superhero(self):

        print(self.name,self.power,self.universe)


super_hero_instance1 = Superhero()
super_hero_instance2 = Superhero()
super_hero_instance3 = Superhero()

super_hero_instance1.set_superhero("Spiderman","spread web","Marvel")
super_hero_instance1.get_superhero()

super_hero_instance2.set_superhero("Batman","fly","DC")
super_hero_instance2.get_superhero()

super_hero_instance3.set_superhero("Minnal Murali","Weight lifting","Basil")
super_hero_instance3.get_superhero()
