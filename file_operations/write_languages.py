languages =["python","java","java script","C#","c++"]
fw = open("file_operations\\languages.txt","w")
for l in languages:
    fw.write(l+"\n")

print("write complete")