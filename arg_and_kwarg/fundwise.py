class Fundwise:

    def __init__(self):
        self.expense=[
                        { "id":21 ,"title":"software engineer","amount":24000,"category":"IT","owner":"Ajna"}
        ]

    def post(self,**kwargs):

        required_fields = {"id","title","amount","category","owner"}

        missing_fields = required_fields.difference(kwargs.keys())

        if missing_fields:

            raise ValueError(missing_fields ,"is missing")    

        self.fundwise.append(kwargs)

        print("records are added ")

fundwise_instance = Fundwise()

fundwise_instance.post(id=210,title="backend developer",amount = 26000,category="IT",owner =" hana")
fundwise_instance.post(id=234,title="hr")