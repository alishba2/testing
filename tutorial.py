#     -----------Function for addition----------------

def addfunction():
    add=(1+2)
    return(add)
#calling function
addition=addfunction()
print(addition)

#    ------------Temperature conversion from C to K-------------

def temp_c_to_k(temp):
    cal= temp + 273
    return(cal)
print("enter temperature in calsius") 
Temp=int(input())
TemperatureK=temp_c_to_k(Temp)
print(TemperatureK)

#     ---------------Making Table--------------

def mytable(tab):
    for x in range(1,11):
        cal = x * tab
        print( x ,"*", tab ,"=" ,cal)
        
#taking input
print("enter the number of table")
x = int(input())
notable=mytable(x)

 