"""
CRUD = create read update delete

create /add = post
list/all = get
detail = retrieve
remove =  delete
update = put
"""

class DietLens:

    def __init__(self):

        self.food_logs=[
                            {"id":21,"name": "dosa","calorie":180,"owner":"hari"}

                        ]
    def post(self,**kwargs):

        required_fields = {"id","name","calorie","owner"}

        missing_fields = required_fields.difference(kwargs.keys())

        if missing_fields:

            raise ValueError(missing_fields ,"is missing")
        # for field in required_fields:

        #     if field not in kwargs:

        #         raise ValueError(field ,"is missing")

        self.food_logs.append(kwargs)

        print("records are added ")

    def get(self):

        if len(self.food_logs)==0:

            print("No records found")

        else:

            for log in self.food_logs:

                print(log)

    def retrieve(self,id=None):

        if not id:

            print("id is missing")

        else:

            return [log for log in self.food_logs if log.get("id")==id]


    def put(self,id=None,**kwargs):

        logs= [log for log in self.food_logs if log.get("id")==id][0]
        logs.update(kwargs)
        print("records has been updated")

    def delete(self,id = None):

        logs= [log for log in self.food_logs if log.get("id")==id][0]
        self.food_logs.remove(logs)
        print("log removed")
        self.get()


diet_instance = DietLens()
diet_instance.post(id = 12,name = "idly",calorie = 200,owner = "Ajna")
# print(diet_instance.retrieve(id = 12))
# diet_instance.put(id=12,name="ghee roast",calorie = 160)
# diet_instance.get()
diet_instance.delete(id = 12)