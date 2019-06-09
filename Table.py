#table
#taking input from user
def table(tab):
    print("----",noTable,"----")
    for x in range(1,11):
        cal = x * tab
        print(x,"*",tab," = ", cal)

print("Enter the number of table")
noTable = int(input())

# call table function
table(noTable)


