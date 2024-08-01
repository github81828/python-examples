


mydict={"brand":"ford","model":"mustang","year":1964}
print(mydict)
#type
type(mydict)
mydict.keys()
mydict.values()
#access
mydict["model"]
mydict.get("model")
#create
phonebook=dict({"name":"ronaldo","country":"portugal","telephone":1234})
print(phonebook)
person=dict([("name","tovino"),("country","india"),("telephone",859030)])
print(person)
marksheet=dict({"name":["hazeeb","anil","sabeetha"],"english":[75,85,68],"maths":[80,85,90]})
print(marksheet)
marksheet["english"]
marksheet["maths"]
#name change
phonebook["name"]="john"
print(phonebook)
#add
phonebook["place"]="kerala"
print(phonebook)
phonebook.update({"place":"perinthalmanna"})
print(phonebook)
phonebook.update({"state":"kerala"})
print(phonebook)
#remove
phonebook.pop("state")
print(phonebook)
phonebook.popitem()
print(phonebook)
del phonebook["name"]
print(phonebook)
#total clear
phonebook.clear()
print(phonebook)
#totol delete
del phonebook
print(phonebook)
#length
len(marksheet)
 #add
print(mydict)
mydict.setdefault("colour","white")
print(mydict)
#copy
mydict2=mydict.copy()
print(mydict2)
dict3=dict(mydict)
print(dict3)
dict4=dict(mydict.items())
print(dict4)
#group dictionary
# each dictionary will store data of a single student
jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

# Outer dictionary to store all student dictionaries (nested dictionaries)
class_six = {'student1': jessa, 'student2': emma, 'student3': kelly}
print("Student 3 name:", class_six['student3']['name'])
print("Student 3 marks:", class_six['student3']['marks'])
print("student 2 name:",class_six["student2"]["name"])
print("student 2 marks:",class_six["student2"]["marks"])
print("\nClass details\n")
#max min
dict1={"c":45,"b":95,"a":35}
print(sorted(dict1.items()))
print(sorted(dict1.values()))
print(sorted(dict1))
print(max(dict1))
print(min(dict1))