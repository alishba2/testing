# Making Function  (use of if and else)
def guess(Guess):
    if"A":
        print("Your Qualities are Coding , Designing and Architecture , Testing and Debuging , Requremint Engg , Quality Insurance")
    elif"B":
        print("Your Qualities are Installing Operating system , Application softwares , Song , Games")
    elif"C":
        print("Your Qualities are Browsing internet , Playing games ")
    else:
        print("Yout Qualities are On and Off")


print("Type of computer users:")
print("A = Computer Programmer")
print("B = Computer Expert")
print("C = Computer users")
print("Enter which kind of user are you")
x = (input())
print(x)
yourQulities = guess(x)
print(yourQulities)

