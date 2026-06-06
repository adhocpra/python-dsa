#create  a dict
student = {
    "name" : "Pravat",
    "age"  : 22,
    "gpa"  : 4,
    "major" : "cs"
}

#access a value
print(student["name"])
print(student["gpa"])
print(student["major"])

#add a key
student["university"] = "NWOSU"
print(student["university"])
student["grade"]= "Senior"
print(student["grade"])

#update the key
student['age']=25
print(student["age"])

#check if exists
print("gpa" in student)
print("job" in student)
print()
#loop through dict
for key, value in student.items():
    print(key, ":",value)

#get all keys and values

print(student.keys())