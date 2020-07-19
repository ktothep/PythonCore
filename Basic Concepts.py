# String
name="karan"
print(name[1:5])
print(name[::-1])
print(name[1:5:2])
print("My name is {name}".format(name=name))
print("My name is {name},{age}".format(name=name,age=23))

#Loops
for i in range(5):
    print(i)

#if Condtions
if name=="karan":
    print("Name matches")
else:
    print("Name different")

#Methods
def square(i):
    return i*i

#Methods with loop
for j in range(5):
    print(j,square(j))

for j in range(3,6):
    print(j,square(j))

#Methods with default value
def multiplier(a,b=0):
    return(a*b)

#Passsing the second Parameter
for j in range(0,6):
    print(multiplier(j,j))

#keeping default value
for j in range(0,6):
    print(multiplier(j))