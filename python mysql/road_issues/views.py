# road_issue_db,
# issues [id,title,location,posted_by,status(unsolved,solved)]

from mysql import connector

class RoadIssuesCreateListDetailUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection = connector.connect(

            user = user,
            password = password,
            host = "localhost",
            database = "road_issue_db"

        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        columns = ""

        for key in kwargs.keys():

            columns += key + ","

        columns = columns.rstrip(",")

        placeholder = ""

        for k in kwargs.keys():

            placeholder = placeholder+"%s,"

        placeholder=placeholder.rstrip(",")

        query = f" insert into issues({columns}) values({placeholder})"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print(".....Issue is added.....")

    def get(self):

        query = "select * from issues"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for issue in records:

            print(issue)

    def retrieve(self,id=None):

        query = " select * from issues where id = %s "

        values = (id,)

        self.cursor.execute(query,values)

        record = self.cursor.fetchone()

        print(record)

    def put(self,id=None,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder+= k + "=%s,"

        place_holder=place_holder.rstrip(",")

        query = f"update issues set {place_holder} where id = %s"

        values = list(kwargs.values())

        values.append(id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("........Records have been updated....... ")

    def delete(self,id=None):

        query = "delete from issues where id = %s"

        values = (id,)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("......Record has been deleted........")

issue_instance = RoadIssuesCreateListDetailUpdateDelete(user="root",password="Password@123")

# issue_instance.post(title="Street light not working",location="Kochi",posted_by="Rahul",status="solved")
# issue_instance.post(title="Garbage accumulation",location="Chalakudy",posted_by="Anjali",status="unsolved")
# issue_instance.post(title="Street garbage not collected",location="Thrissur",posted_by="Kiran",status="unsolved")
# issue_instance.post(title="Public toilet needs maintenance",location="Kottayam",posted_by="Neha",status="unsolved")
# issue_instance.post(title="Broken traffic signal",location="Kochi",posted_by="Meera",status="solved")
# issue_instance.post(title="Broken park bench",location="Thrissur",posted_by="Amal",status="solved")
# issue_instance.post(title="noise pollution near school",location="Thrissur",posted_by="aneesh",status="solved")
issue_instance.get() 
# issue_instance.retrieve(3)

# issue_instance.put(3,location ="kannur",posted_by = "Ajna")

# issue_instance.delete(7)


