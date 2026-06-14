#linear search checks every item so slow 
#binary search cuts in half
#for Binary search list must be sorted first

#1 Find the index of the target
def binary_search(lst,target):
    left=0
    right= len(lst)-1

    while left <=right:
        mid =(left+right)//2
        if lst[mid]== target:
            return mid
        elif lst[mid]<target:
            left= mid+1
        else:
            right= mid-1
    return -1

numbers = [2,5,8,12,16,23,38,45]
print(binary_search)
print (binary_search(numbers,23))
print()
# Given a sorted list and a target,
# if target exists → return its index
# if target does NOT exist → return the index where it SHOULD be inserted

numbers = [1, 3, 5, 7, 9, 11]

# Test 1: binary_search(numbers, 7)  → 3  (exists at index 3)
# Test 2: binary_search(numbers, 6)  → 3  (should be inserted at index 3)
# Test 3: binary_search(numbers, 0)  → 0  (should be inserted at index 0)
# Test 4: binary_search(numbers, 15) 
# 6  (should be inserted at end)

def bs_1(lst,target):
    left=0
    right= len(lst)-1

    while left<=right:
        mid= (left+right)//2
        if lst[mid] == target:
            return mid
        elif lst[mid]<target:
            left=mid+1
        else:
            right= mid-1
    return left #
numbers= [1,3,5,7,9,11]
print(bs_1(numbers,7))
print(bs_1(numbers,6))
print(bs_1(numbers,0))

print(bs_1(numbers,15))


#3.# Given a sorted list, count how many times target appears.


numbers = [1, 3, 5, 5, 5, 7, 9, 11]

# Test 1: count(numbers, 5)  → 3
# Test 2: count(numbers, 7)  → 1
# Test 3: count(numbers, 4)  → 0

def find_first(lst,target):
    left=0
    right=len(lst)-1
    result=-1 #ass
    while left<=right:
        mid=(left+right)//2
        
        if lst[mid]== target:
            result=mid #save position
            right= mid-1 #search for earlier concurremce
        elif lst[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return result

def find_last(lst,target):
    left=0
    right=len(lst)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        
        if lst[mid]==target:
            result=mid
            left=mid+1
        elif lst[mid]< target:
            left=mid+1
        else:
            right=mid-1
    return result
def count(lst, target):
    first=find_first(lst,target)
    if first==-1:
        return 0
    last= find_last(lst,target)
    return last-first+1

numbers= [1,3,5,5,5,7,9,11]
print(count(numbers,5))
print(count(numbers,7))
print(count(numbers,0))


