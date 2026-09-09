from mysql import connector

class ExpenseCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection = connector.connect(

            user = user,
            password=password,
            host= "localhost",
            database = "tripwise_db"
            
        )

        self.cursor = self.connection.cursor()


    def post(self,**kwargs):

        query=" insert into expense (trip,paid_by,amount,category) values(%s,%s,%s,%s);" 

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print(".....Expense is added.....")


    def get(self):

        query = "select * from expense"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for exp in records:

            print(exp)

    def retrieve(self,id=None):

        query = "select * from expense where id =%s"  

        values = (id,)  

        self.cursor.execute(query,values)

        record = self.cursor.fetchone()

        print(record)

    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder += k + "=%s,"

        place_holder=place_holder.rstrip(",")

        query = f"update expense set {place_holder} where id=%s"

        values=list(kwargs.values())
        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("......record has been updated........")

expense_instance = ExpenseCreateListRetrieveUpdateDelete(user="root",password="Password@123")

#print(expense_instance.connection)

#expense_instance.post(trip="manali",paid_by="hiba tharakan",amount=3200,category="food")
#expense_instance.get()
expense_instance.retrieve(2)
expense_instance.put(id = 2,trip ="kerala - banglore",amount = 3500)