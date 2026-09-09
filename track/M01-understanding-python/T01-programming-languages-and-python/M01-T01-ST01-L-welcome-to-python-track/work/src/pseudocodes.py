# To Print hello world
#start
#print("hello world")
#end
print("Hello world \nThank you for learning Python")
print("Hello World" , end=" - ")
print("Thank you for learning Python")
name = "Raghuvarmaraju"
print("Name:\t",name)
# To find whether number (N) is even or odd

#START
    #READ N
    #IF N % 2 == 0 THEN
     #   Display "Even"
   # ELSE
    #    Display "Odd"
    #END IF
#STOP
n = 10 
if n%2 == 0:
    print("even")
else:
    print("odd")    


# To find the number is pos, neg or Zero
#START
  #READ N
    #IF N > 0 THEN
      #  Display "Positive"
    #ELSE IF N < 0 THEN
    #    Display "Negative"
    #ELSE
     #   Display "Zero"
    #END IF
#STOP
n = 10
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")   
       

# To find the largest among 3 numbers a, b , c
#START
 #   READ a, b, c
    #IF a >= b THEN
       # IF a >= c THEN
          #  Display a, "is the largest"
        #ELSE
          #  Display c, "is the largest"
       # END IF
    #ELSE
        #IF b >= c THEN
           # Display b, "is the largest"
        #ELSE
          #  Display c, "is the largest"
       # END IF
    #END IF
#STOP
a = 10
b = 20
c = 30
if a>=b:
    if a>=c:
        print(a,"is the largest")
    else:
        print(c,"is the largest")
else:
    if b>=c:
        print(b,"is the largest")
    else:
        print(c,"is the largest")       