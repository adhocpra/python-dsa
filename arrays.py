#create a list
numbers = [5,3,8,1,9,2,7]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])


print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

#-- list operations'

fruits= ["apple","banana","mango"]
fruits.append("grape")
fruits.insert(1,"orange")
fruits.remove("banana")
fruits.pop()#removes last item in the list
print("mango" in fruits)
print("grape" in fruits)

for fruit in fruits:
    print(fruit)
print(fruits)


#numbers
numbers= [1,2,3,4,5,6,7,9]
square= [n**2 for n in numbers]
print(square)

tripled= [n*3 for n in numbers]
print(tripled)

even= [ n for n in numbers if n%2==0]
print(even)

odd = [n for n in numbers if n%2!=0]
print(odd)

even_square= [n**2 for n in numbers if n%2==0]
print(even_square)

#convert into strings
str= [str(n) for n in numbers]
print(str)

grt= [ n for n in numbers if n>5]
print(grt)