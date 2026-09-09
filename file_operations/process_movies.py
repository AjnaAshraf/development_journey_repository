fr = open("file_operations\\movie.csv","r",encoding="utf-8")

movies=[]

for line in fr:

    line= line.rstrip("\n")

    id,title,language,year,run_time,rating,genre = line.split(",")

    movie_dictionary = {

                        "id":id,"title":title,"language":language,
                        "year":year,"run_time":run_time,"rating":rating,
                        "genre":genre
    }

    movies.append(movie_dictionary)

print(len(movies))