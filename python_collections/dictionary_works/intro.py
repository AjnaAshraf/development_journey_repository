"""
    dictionary
    ==========

    define = {key:value,key:value}
    ie,{"name":"ajna","course":"python django","class":"c2"}

    mutable:yes

    ordered:

    duplicates: duplicate keys not allowed

    methods:
             keys()--- display all keys in the dict
             values() --- display all values in the dict
             items()---- to display all the keys and values together
             get(key)-----to get the value using key (),better than using dict_name.[key] since if we write any non exist key it will display error ,using get the output will be none
            
"""

daily_calories = {
                  "mon":2000,"tues":2300,
                  "wed":1900,"thurs":1500,
                  "fri":2000,"sat":2100,
                  "sun":1400
                  }

print(daily_calories["thurs"])
daily_calories["mon"]=1600
print(daily_calories)


print(daily_calories.keys())
print("========all keys=======")

for k in daily_calories.keys():
    print(k)
print("========all values=======")
for v in daily_calories.values():
    print(v)

print("=====keys and values=======")

for k,v in daily_calories.items():
    print(k ,v)

print(daily_calories.get("total"))# will display none as output
print(daily_calories.get("total",0))# here total is not a key in 
# the dictionary so it will return zero since we mentioned it in the code ,otherwise the answer for non existed key is "None"
print(daily_calories.get("tues",0))

daily_calories["total calorie"] = sum(daily_calories.values())

print(daily_calories)