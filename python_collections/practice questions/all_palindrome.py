words = ["madam","malayalam","ant","tan","racecar"]

palindrome_list = []

for w in words:

    reversed = w[::-1]

    if reversed == w:

        palindrome_list.append(w)
        
print(palindrome_list)
