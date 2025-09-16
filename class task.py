# class task 1

print("Hello world!")

# class task 2

name1 = "Harry"
name2 = "John"
print(name1)
print(name1,name2)
print(name2)
print(name1, name2)
print (name1, "is eating ice cream with" , name2)
print (name1, "and" ,name2 , "are friends")

# class task 3

Name = input("What is your name: ")
print(f"Hi there {Name}")

# class task 4

Num1 = 47
Num2 = 102
Sum = Num1 + Num2
Diff = Num2 - Num1
Product = Sum * Diff
print(f"{Num1} + {Num2} = {Sum}")
print(f"{Num2} - {Num1} = {Diff}")
print(f"{Sum} * {Diff} = {Product}")
print (f" {Num1} + {Num2} = {Sum}, {Num2} - {Num1} = {Diff}, {Sum} * {Diff} = {Product}")

# test task 1


print("Calculate the area of a wall.")
feed = input("Enter the width in meters: ")
width = int(feed)

feed = input("Enter the height in meters: ")
height = int(feed)

print(f"Width is {width} m and height is {height} m.")
area = width * height

print(f"The wall will be {area} square meters.")


# test task 2

feed = input("Insert an integer: ")
value = int(feed)

remainder = value % 2


print(f"Value is {value}")
print(f"The remainder is {remainder} when {value} is divided by 2.")
