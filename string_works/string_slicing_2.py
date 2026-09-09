text = "A man, a plan, a canal panama"
#       01234567890123456789012345678
#                 1         2


# extract canal

substring = text[17:22]
print(substring)

# extract plan

substring2 = text[9:13]
print(substring2)

# extract panama

substring3 = text[23:]
print(substring3)


#extract a man

substring4 = text[:5]
print(substring4)


copy_string = text[:]
print(copy_string)