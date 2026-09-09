class Phone:

    name:str
    Brand : str
    price:int
    color:str
    storage:int

    def call(self):

        print("phone is ringing")

    def msg(self):

        print("texting.......")

    def game(self):

        print("playing gamess...")


phone1 = Phone()
phone2 = Phone()
phone3 = Phone()
phone4 = Phone()

phone1.msg()
phone2.game()
phone3.call()
