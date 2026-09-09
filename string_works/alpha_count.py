""" wap  for alpha_count and digit_count in text """

text = "england won by 6 wickes with 3 balls remaining. england leads the series with 2 - 1"
alpha_count = 0
digit_count=0
special_char_count=0
for ch in text:

    if ch.isalpha():

        alpha_count=alpha_count+1
    
    elif ch.isdigit():

        digit_count = digit_count+1

    else:

        special_char_count = special_char_count+1

print(alpha_count)
print(digit_count)
print(special_char_count)
