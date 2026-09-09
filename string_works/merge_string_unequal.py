#word_1 = "PQRST"
#          01234
#word_2 = "ABC"
#          012

def merge_str(word1,word2):

    result = ""
    max_str = max(word1,word2,key=len)

    for i in range(0,len(min(word1,word2,key=len))):

        result += word1[i]+word2[i]
    balance = max_str[len(min(word1,word2,key=len)):]
    result+=balance
    print(result)


merge_str("PQRST","ABC")


##-------OR-------
##-------OR-------
##-------OR-------
##-------OR-------
##-------OR-------


def is_merge_str(word1,word2):

    merge_str=""
    small_str=""
    large_str=""

    if len(word1) > len(word2):
        small_str = word2
        large_str = word1

    else :
        small_str = word1
        large_str = word2


    for i in range(0,len(small_str)):

        merge_str += word1[i]+word2[i]

    balance = large_str[len(small_str):]

    merge_str+=balance

    print(merge_str)
    

is_merge_str("PQRST","ABC")