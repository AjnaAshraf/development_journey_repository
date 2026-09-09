"""
design and create a simple python crud application of movie each movie with attributes
# id,title,year,genre,rating,run_time,director

"""

class Movies:

    def __init__(self):

        self.movies = [

            {"id": 1,"title":"Athiradi","year":2026,"genre":"Entertainment","rating":7.8,"run_time":"2h 30m","Director":"Ajna"}
        ]

    def post(self,**kwargs):

        required_field = {"id","title","year","genre","rating","run_time","Director"}

        missing_fields = required_field.difference(kwargs.keys())

        if missing_fields:

            raise ValueError(missing_fields, " is missing ")

        self.movies.append(kwargs)

        print("movie records has been added.....")

    def get(self):

        if len(self.movies)==0:

            print("No Records Found")

        else:

            for movie in self.movies:

                print(movie)

    def retrieve(self,id = None):

        movie = [m for m in self.movies if m.get("id")==id][0]

        print(movie)

    def put(self,id=None,**kwargs):

        movie = [m for m in self.movies if m.get("id")==id][0]

        movie.update(kwargs)

        print("Movie Record has been updated")

        print(movie)

    def delete(self,id=None):

        movie = [m for m in self.movies if m.get("id")==id][0]

        self.movies.remove(movie)

        print("movie record has been deleted ")

        self.get()

movie_instance = Movies()
movie_instance.post(id =2,title ="Manichitrathazhu" ,year = 1993,genre ="Psychological Thriller",rating =9.1,run_time = "2h 49m",Director = "Fasil")
movie_instance.post(id =3,title ="Spider-Man: Brand New Day",year = 2026,genre ="Action/Adventure ",rating =8.1,run_time = "2h 30m",Director = "Destin Daniel Cretton")
#movie_instance.get()
movie_instance.retrieve(id=3)
movie_instance.put(id=1,Director ="Arun Anirudhan")
movie_instance.delete(id=2)

       






        