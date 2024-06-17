dic = {
    "Ram": "A human name",
    "apple": "A fruit"

}

print(dic["Ram"])

print(dic.get("apple"))

print(dic.keys())
print(dic.values())
print(dic.items())

for key in dic.keys():
    print(dic.get(key))

for key , val in dic.items():
    print(f"{key} is {val}\n")


# print(dic.pop("Ram"))
# dic.pop("Ram")
dic.popitem()
print(dic)