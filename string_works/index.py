"""
syntax :  

string_object.index(char)

string_object.startswith("substring")

string_object.endswith("substring")

string_object.replace(old,new) # replace old string with new
string_object.strip(value)# remove value from both ends
string_object.lstrip(value)# remove value from beginning
string_object.rstrip(value)# remove value from end


"""

name = "alicent"

print(name.index("i")) # will return the index value of the number ,if the character is doesnt exist then returns error 

print(name.startswith("al"))# checks whether the string object starts with the substring 

print(name.endswith("nt"))# checks whether the string object ends with the substring 
print(name.endswith("n"))

text = "I love ajna"

new_txt = text.replace("love","adore") # replace old string with new
print(new_txt)
print(text.replace("love","hate"))

company = "@luminar technolab@"

print(company.strip("@")) # remove value from both ends
print(company.lstrip("@")) # remove value from beginning
print(company.rstrip("@")) # remove value from end

print("a" in "apple")
