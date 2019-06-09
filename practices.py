#python operators
#Arithmatical operations
num1=3
num2=2
add=(num1+num2)
sub=num1-num2
multi=num1*num2
div=num1/num2
mod=7%8
expo=9**2
print(mod)
print(expo)
print(add)
print(multi)
print(sub)
print (div)
#assignment operators
x=3
print(x)
x+=3
print(x)
x-=5
print(x)
x*=3
print(x)
x%=1
print(x)
#python comparison operators
x=3
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
#python logical operartors
x=3
y=6
print(x>=y and x>y)
print(x>y or x<y)
print(not(x<2 or x>1))
#python string
print("alishba")
a="maemoona"
print(a[4])
print(a[3:5])
x=" nnn "
print(x.strip())
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("m" , "n"))
#python list
mylist=["pizza","burger","fries"]
print(mylist)
print(len(mylist))
print(mylist[1])
mylist[1]= "shawarma"
print(mylist)
for x in mylist:
  print(x)
if "pizza" in mylist:
    print(" yes 'pizza' is in mylist")
mylist.append("chicken")
print(mylist)
mylist.insert(1,"orange")
print(mylist)
mylist.remove("pizza")
print(mylist)
mylist.pop()
print(mylist)
del mylist[1]
print(mylist)
mylist.clear()
print(mylist)
thislist=mylist.copy()
print(thislist)
#python if and else operators
a=4
b=8
if b > a:
    print("b is greater than a")
x=3
y=3
if x > y:
    print("x is greater than y")
elif x<y:
     print("x is smaller than y")
else:
    print("x is equal to y")
#for loop
for x in "banana":
  print(x)
name=["alishba","moona","afzaal","bilal"]
for x in name:
    print(x)
for x in name:
    if x=="moona":
        continue
    print(x)
for x in range (6):
    print(x)
for x in range(2,4):
    print(x)
for x in range(6):
    print(x)
else:
    print("finally finished")
fruit=["apple","cherry","orange"]
adj=["big","sweet","fresh"]
for x in fruit:
    for y in adj:
        print(x,y)
#python function
def my_function():
    print("hello")
def my_function(name):
    print(name +  "Arshad")

my_function("Alishba")
my_function("Maemoona")
my_function("Bilal")
my_function("Afzaal")
def my_function(country="england"):
    print("i am from" +   country)
my_function("norway")
my_function("pakistan")
my_function()
def my_function(food):
    for x in food:
        print(x)
fruit=["banana","apple","orange"]
my_function(fruit)
veg=["capcicum","cabage","carrot"]
my_function(veg)
def my_function(x):
    return 4 * x
print(my_function(3))
print(my_function(3))
print(my_function(2))

    





