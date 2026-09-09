

def is_pangram(text):

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for ch in alphabets:

        if ch not in text.lower():

            print(False)
            break

    else:

        print(True)

is_pangram("the quick brown fox jumps over the lAzy dog" )
is_pangram("ffdyhjk")