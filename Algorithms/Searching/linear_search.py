def liner_search(lst,target):
    for i in range(len(lst)):
        if lst[i]== target:
            return i #return the index where found
    return -1 #-1 means not found
my_list= [1,3,5,7,11,13,17]
print(liner_search(my_list,11))
print(liner_search(my_list,21))

#1.Find if name exists
def name_exists(names, target):
    for i in range(len(names)):
        if names[i] == target:
           return f"Found {target} at index {i}"
    return -1
names= ["Pat", "Vat", "Rat", "cat"]
print(name_exists(names, "Rat"))
print(name_exists(names, "Ronaldo"))

#2.Find all occurance
def occurance(lst,target):
    indexes =[]
    for i in range(len(lst)):
        if lst[i]==target:
            indexes.append(i)
    return indexes
numbers=[4,2,7,2,9,2]
print(occurance(numbers,2))

#Find largest in list w/o max
def largest(lst):
    largest= lst[0]
    for i in range(len(lst)):
        if lst[i]>largest:
            largest= lst[i]
    return largest
numbers= [3,1,8,2,6]
print(largest(numbers))

