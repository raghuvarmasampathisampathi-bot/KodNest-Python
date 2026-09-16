#Selection Statements
#if statement
age = 19
if(age>=18):
    print("eligible to vote")

#if-else statement
age = int(input("enter the age"))
if(age>=18):
    print("eligible for vote")
else:
    print("not eligible for vote")



#if-elif-else ladder

#Write a Python program to accept marks and print the grade using the following conditions:#90+ → A, 70+ → B, 50+ → C, 35+ → D, otherwise → Fail.
marks = int(input("enter your marks:"))
if(marks>=90):
    print("Grade A")
elif(marks>=70):
    print("Grade B")
elif(marks>=50):
    print("Grade C")
elif(marks>=35):
    print("Grade D")
else:
    print("Fail")


#Nested if statement
#Write a Python program to check whether you are free tonight. If you are free, check whether your friends are available. Print "Go out for party" if both are true; otherwise print the appropriate message.
free_tonight=True
friends_available = True
if(free_tonight):
    if(friends_available):
        print("Go out for party")
    else:
        print("Stay at home for a movie night")
else:
    print("Will catch up next time")
    

#match-case with multiple cases
#Write a Python program that accepts a number from 1 to 7 and uses match-case to print the corresponding day of the week.
day = int(input("enter the number between 1 and 7"))
match(day):
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

#match-case with multiple cases
#Write a Python program that accepts a month number and uses match-case to print the season: 3,4,5 → Summer, 6,7,8 → Rainy, 9,10,11,12 → Winter, and 1,2 → Autumn.
month = int(input("enter the month number between 1 and 12"))
match(month):
    case 3|4|5:
        print("Summer")
    case 6|7|8:
        print("Rainy")
    case 9|10|11|12:
        print("Winter")
    case 1|2:
        print("Autumn")
    case _:
        print("Invalid month")



#for loop with range
#Write a Python program to print numbers from 1 to 5 using a for loop


