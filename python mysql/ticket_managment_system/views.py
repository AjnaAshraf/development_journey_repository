from mysql import connector

class TicketCreateListRetriveUpdateDelete:

    def __init__(self,user = None,password = None):

        if user == None or password == None:

            raise Exception ("....Username and password required.....")

        self.connection = connector.connect(

            user = user,
            password = password,
            host = "localhost",
            database = "customer_support_db"

        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        db_col =("customername","email","subject","description","category","priority","status","assigned_to")

        difference = set(db_col).difference(kwargs.keys())

        if difference:

            raise Exception(f"{difference} required")

        col_str = ",".join(db_col)

        query = f"insert into supportticket ({col_str}) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("...record has been added....")

    def get(self):

        query =" select * from supportticket"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for ticket in records:

            print(ticket)

    def retrieve(self,id=None):

        query = " select * from supportticket where id = %s"

        values = (id,)

        self.cursor.execute(query,values)

        ticket = self.cursor.fetchone()

        print(ticket)

    def put(self,id=None,**kwargs):

        placeholder = ""

        for k in kwargs.keys():

            placeholder += k + "=%s,"

        placeholder=placeholder.rstrip(",")

        query = f"update supportticket set {placeholder} where id = %s"

        values=list(kwargs.values())

        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

    def delete(self,id = None):

        query = "delete from supportticket where id = %s"

        values = (id,)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("..... the record has been deleted .....")

    def filter(self,**kwargs):

        place_holder = "" 

        for k in kwargs.keys():

            place_holder+= k+ "=%s and "

        place_holder = place_holder.rstrip("and ")

        query = f" select * from supportticket where {place_holder} "

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        records = self.cursor.fetchall()

        if records :

            for t in records:

                print(t)

        else:

            print(".....NO RECORDS....")

    def summary(self):

        query = "select status,count(*) as count from supportticket group by status"

        self.cursor.execute(query)

        response = self.cursor.fetchall()

        print(response)

        priority_query = "select priority,count(*) as count from supportticket group by priority"

        self.cursor.execute(priority_query)

        priority_summary = self.cursor.fetchall()

        print("priority summary",priority_summary)

ticket = TicketCreateListRetriveUpdateDelete(user="root",password="Password@123")

# print(ticket.connection)

# ticket.post(customername="Arun",email="arun123@gmail.com",subject="payment deducted but order pending",description="i made the payment yesterday but my order is still showing pending.........",category="payment",priority="high",status="open",assigned_to="rahul")
        

# ticket.post(
#     customername="Meera",
#     email="meera456@gmail.com",
#     subject="Unable to login",
#     description="I am unable to log in to my account even after entering the correct password.",
#     category="account",
#     priority="medium",
#     status="inprogress",
#     assigned_to="sneha"
# )
# ticket.post(
#     customername="Rahul",
#     email="rahul789@gmail.com",
#     subject="Order not delivered",
#     description="My order was supposed to be delivered two days ago but I have not received it yet.",
#     category="delivery",
#     priority="high",
#     status="resolved",
#     assigned_to="arjun"
# )

# ticket.post(
#     customername="Anjali",
#     email="anjali321@gmail.com",
#     subject="Wrong product received",
#     description="I received a different product from the one I ordered. Please help me with the replacement.",
#     category="delivery",
#     priority="medium",
#     status="open",
#     assigned_to="rahul"
# )

# ticket.post(
#     customername="Sneha",
#     email="sneha333@gmail.com",
#     subject="Discount coupon not working",
#     description="The discount coupon I received is not being applied during checkout.",
#     category="payment",
#     priority="medium",

#     assigned_to="sneha"
# )

# ticket.get()
# ticket.retrieve(4)
# ticket.put(id = 6,customername = "Hiba",status = "inprogress")
# ticket.retrieve(6)

# ticket.delete(5)

# ticket.filter(customername="Anjali")

ticket.summary()