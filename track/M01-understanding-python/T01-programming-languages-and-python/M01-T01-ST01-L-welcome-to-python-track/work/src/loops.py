#for loop with range
#Write a Python program to print numbers from 1 to 5
for i in range(1,6):
    print(i)

#for loop with if condition
#write a python program to print even numbers between 1 to 10
for i in range(1,11):
    if i%2 == 0:
        print(i)

#while loop
#write a python program to print numbers from 0 to 4 using while loop
i = 0
while(i<5):
    print(i)
    i = i+1   

#jumping statements

#break statement
#write a python program to print numbers from 1 to 10 and break the loop when the number is 5
for i in range(1,11):
    if i == 5:
        break
    print(i)

#continue statement
#write a python program to print numbers from 1 to 10 and continue the loop when the number is 5
for i in range(1,11):
    if i == 5:
        continue
    print(i)