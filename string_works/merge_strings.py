"""
merge strings

 word_1 ="PQRS"
 word_2 = "ABCD"
"""
word_1 ="PQRS"
word_2 = "ABCD"
merged_str=""
for i in range(0,4):
    merged_str += word_1[i] + word_2[i]
print(merged_str)

print(len(word_1))