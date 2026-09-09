

def is_anagram(word_1,word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    
    for ch in word_1:

        if ch not in word_2 or word_1.count(ch)!= word_2.count(ch):

            print(False)
            break

    else:

        print(True)

is_anagram("thing","night")
is_anagram("silent","listens")
is_anagram("fiRed","fried")
