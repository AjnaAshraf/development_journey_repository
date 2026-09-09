movies=[
            ["kgf","kannada",150,2023,8],
            ["balan","malayalam",160,2026,7],
            ["athiradi","malayalam",180,2025,8],
            ["ramayan","hindi",160,2026,9],
            ["goatlife","malayalam",180,2026,8],
            ["spiderman:brand new day","english",180,2027,9]
]

#display runtime,yr,rating of goatlife

print(movies[4][2: ])

#display all movies_title

titles=[m[0] for m in movies]
print(titles)

#display all movie yr
all_yr = {m[3] for m in movies}
print(all_yr)

#display all movie language
language= {m[1] for m in movies}
print(language)
