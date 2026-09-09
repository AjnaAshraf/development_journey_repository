word = "pneumonoultramicroscopicsilicovolcanoconiosis"
vowel_count = 0
consonants_count=0
for ch in word:

    if ch.isalpha():
        if ch in "aeiouAEIOU":

            vowel_count=vowel_count+1
        else:

            consonants_count = consonants_count+1


print(f"consonant count is : {consonants_count}")
print(f"vowel count is : {vowel_count}")
