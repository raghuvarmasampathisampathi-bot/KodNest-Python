names = ("Allice","Bob","Charlie","Bob")
print(names)
print(names,type(names))
print(len(names))
print(names.count("Bob"))
print(names.index("Bob"))
print(names[3])
print(names[-1])
yn = names[0:3]
print(yn,type(yn))

#loop
for n in names:
    print(n)

fruits =("apple",)
print(fruits * 3,type(fruits))

#constructors
stu_info = tuple(["Alice", 15, 23000, True])
print(stu_info, type(stu_info))

n = 10
print(n,type(n))
numbers = 1, 2, 3, 4, 5
print(numbers,type(numbers))
#numbers[1] = 200 # immutable
del numbers
#print numbers

age =[10,20]
age[1] = 25
print(age)

#tuple unpacking
fruits = ("apple","banana","cherry")
(f1, *f2) = fruits
print(f1)
print(f2,type(f2))

#packing
a = 10
b = 20
c = 30
numbers = (a, b, c)
print(numbers,type(numbers))


a = (1, 2, 3)
b = (4, 5, 6, 7, 8)
c = a + b
print(c, type(c))
