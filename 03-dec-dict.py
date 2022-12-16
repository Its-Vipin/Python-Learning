# myDict={
#     'name':'Vipin',
#     'age':"19",
# }
# # print(myDict['name'])
# # a=myDict.get("age")
# # print(a)
# # keys=myDict.keys()
# # values=myDict.values()
# # print(keys)
# # print(values)
# # items=myDict.items()
# # print(items)
# # print(myDict.popitem())
# # print(list(items))

# myDict.update({
#     "age":33
# })
# myDict.pop('name')
# print(myDict)

# d1={"one":1,"two":2,"three":3}
# d2={"four":4,"five":5,"six":6}

# d1.update(d2)
# print(d1)

dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}

a=dict1["class"]
b=a["student"]
c=b["marks"]
d=c["web"]
print(d)

print(dict1["class"]["student"]["marks"]["web"])