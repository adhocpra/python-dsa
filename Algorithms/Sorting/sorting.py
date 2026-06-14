#sorting

scores= [85,42,91,67,23]

#1. Ascending
print(sorted(scores))
print(scores)
print(scores.sort())

#2.Descending
print(sorted(scores, reverse=True))

#3.Alphabetically
names= ["bob", "callice","daug","yak","honey","brown","allis"]
print(sorted(names))

#4.Sorting with lenth
print(sorted(names, key=len))

#5.IN place

#searching
#linear and binary

students= ["ram", "shyam", "Pravat", "John"]

def find_student(names, target):
    for i in range (len(names)):
        if names[i] ==target:
            print(f"found at position {i}")
            return
    print("Not found")
find_student(students, "Pravat")
