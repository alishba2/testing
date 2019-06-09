#grade calculation

# add subject marks
def addSubject(Math , English , Computer , Urdu , Islamiat , physics):

    cal = (Math + English + Computer + Urdu + Islamiat + physics)
    return cal

# percentage 
def percentage(marks):

    Totalmarks = 520
    Per = marks / Totalmarks
    percentage = Per * 100
    return percentage

# Grading 
def grade(percentage):
    
    if percentage > 90 :
        print("your grade is A+")
    elif percentage > 80 :
        print("your grade is A")
    elif percentage > 70:
        print("your grade is B")
    elif percentage > 60 :
        print("your grade is c")
    else:
        print("you are fail")   


#Taking subject input
print("Enter your math grades")
Math = int(input())
print("Enter your english grades")
English = int(input())
print("Enter your computer grades")
Computer = int(input())
print("Enter your urdu grades")
Urdu = int(input())
print("Enter your Islamiat grades")
Islamiat = int(input())
print("Enter your physics grades")
physics = int(input())


# call add subject marks 
ObtainMarks = addSubject(Math , English , Computer , Urdu , Islamiat , physics)
# call percentage 
percentageMarks = percentage(ObtainMarks)
# call grading 
grade(percentageMarks)





