print("Enter Marks Obtained in 3 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
tot = markOne+markTwo+markThree
avg = tot/3

if avg>=70 and avg<=100:
print("Your Grade is A")
elif avg>=60 and avg<70:
print("Your Grade is B")
elif avg>=50 and avg<60:
print("Your Grade is C")
elif avg>=40 and avg<50:
print("Your Grade is D")
elif avg>=0 and avg<40:
print("Your Grade is Fail")
else:
print("Invalid Input!")

