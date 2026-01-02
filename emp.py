dict1 = {'EmpNo':'532','EmpName': 'Naveen', 'EmpAge': 21, 'EmpCity': 'Hyderabad'}
print("\n Dictionary is :",dict1)
print("\n Employee Name is :",dict1['EmpName'])
print("\n Employee City is :",dict1['EmpCity'])
print("\n All Keys in Dictionary ")
for x in dict1:
    print(x)
print("\n All Values in Dictionary ")
for x in dict1:
    print(dict1[x])
dict1["Phno"]=85457854
print("\n Updated Dictionary is :",dict1)
dict1["EmpName"]="Madhu"
print("\n Updated Dictionary is :",dict1)
dict1.pop("EmpAge")
print("\n Updated Dictionary is :",dict1)
print("Length of Dictionary is :",len(dict1))
dict2=dict1.copy()
print("\n New Dictionary is :",dict2)
dict1.clear()
print("\n Updated Dictionary is :",dict1)
