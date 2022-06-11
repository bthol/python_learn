# string concatenation
name = "Blake"
stringy = "Hello, my name is " + name
print(stringy)

# variabes and reassinment
x = "original string"
print(x)
x = "new string"
print(x)

# functions, arguments and calling functions
def funct1(y):
    z = y
    print(z)
funct1("pass")

# arrays and accessing items
arr = [-1, -2, 2, 1]
arr7 = [7, 7, 7, 7, 7, 7, 7, 0]
print(arr[sum(arr) - 3])
print(arr[len(arr) - 1])
print(arr7[len(arr7) - 1])

#conditional statements
condition = 1
# condition = 2
# condition = "carrots"
if condition == 1:
    print("First")
elif condition == 2: 
    print("Second")
else:
    print("else")

