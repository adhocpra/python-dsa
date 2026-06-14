numbers = [10,20,30,40,50]

for num in numbers:
    print(num)
print()
for i in numbers:
    print(i+5) #this both same
print()
for i in range(len(numbers)):
    print (i,numbers[i])
print()
def add_five(numbers):
    for i in numbers:
        print(i+5)
my_list= [10,20,30,40,50]
add_five(my_list)

print()
def multiply_two(numbers):
    for i in numbers:
        print(i*2)
my_list= [3,6,9,12,15]
multiply_two(my_list)

def print_even(numbers):
    for i in numbers:
        if(i%2==0):
            print (i)

my_list= [1,2,3,4,5,6,7,8,9]
print_even(my_list)

def print_add(numbers):
    total=0
    for i in numbers:
        total = total+i
        print(total)
               
my_list= [1,2,3,4,5]
print_add(my_list)

def find_largest(numbers):
    largest = numbers[0]
    for i in numbers:
        if i>largest:
            largest =i
            print(largest)
my_list=[3,9,7,4,10]
find_largest(my_list)

def count_numbers(numbers,target):
    count=0
    for i in numbers:
        if i ==target:
            count= count+1
            print(count)                  
my_list= [1,3,3,5,3,4,3]
count_numbers(my_list,3)

def greater_than_ten(numbers):
    for i in numbers:
        if  i >10:
            print(i)
my_list=[0,1,4,9,11,23,34]
greater_than_ten(my_list)

#list of numbers and returns a new list with name starting with A

def starts_with_A(names):
    result=[]
    for name in names:
        if name[0]== "A":
           result.append(name)
    return result
my_list = ["Alice", "BOB", "arsnal"]
print(starts_with_A(my_list))

def odd_number(numbers):
    result=[]
    for num in numbers:
        if num % 2 != 0:
            result.append(num)
    return result
my_list =[1,2,3,4,5,6,7]
print(odd_number((my_list)))

def odd_number(numbers):
    result=[]
    for num in numbers:
        if num % 2 != 0:
            result.append(num*3)
    return result
my_list =[1,2,3,4,5,6,7]
print(odd_number((my_list)))

def combine_lists (list1,list2):
    result =[]
    for i in list1:
        result.append(i)
    for i in list2:
        result.append(i)
    return result
list1= [1,2,3]
list2= [4,5,6]
print(combine_lists(list1,list2))

def find_name(names, target):
    for name in names:
        if name==target:
            return("Found")
    return False
my_list= ["Pravat", "Rohan", "Messi"]
print(find_name(my_list, "Pravat"))
print(find_name(my_list, "alice"))
        
#second largest in the list
def second_largest(numbers):
    largest= numbers[0]
    second= numbers[1]
    if second>largest:
        largest, second = second, largest
    