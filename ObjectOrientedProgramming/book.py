class Books:

    title:str
    price:float
    author:str
    pages:int

    def __init__(self,title,price,author,pages):

        self.title=title
        self.price=price
        self.author=author
        self.pages=pages

    def get_book(self):

        print(self.title,self.price,self.author,self.pages)


it_ends_with_us =Books("it ends with us",350,"helleen",560)
it_ends_with_us.get_book()