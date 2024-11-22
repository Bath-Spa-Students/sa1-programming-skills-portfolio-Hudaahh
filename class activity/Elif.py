#ELIF
a = 300
b = 300
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#practice time
#make the user to input the score
mark=int(input("Enter the mark"))
#outputs a if it is greater than or equal to 90
if mark>= 90:
  print("your grade is A")
#check if the score is above or equal to 80
elif mark>=80:
    print("your grade is B")
#check if the mark is above or equal to 70
elif mark<=70:
    print("your grade is C")
#outputs D if its above or equal to 60
elif mark>=60:
    print("your  grade is E")
#prints F its less than 60
else:
  print("your grade is F")
