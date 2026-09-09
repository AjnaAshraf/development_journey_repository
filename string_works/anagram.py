word_1 = "silents"
word_2 = "listen"

for ch in word_1:

    if ch not in word_2 or word_1.count(ch)!= word_2.count(ch):

        print("not an anagram")
        break

else:

    print("ANAGRAM")