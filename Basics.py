# print("Helllo HCIA PDTP-Huawei Team")
num1 = 12
num2 = 8
sum = num1 + num2
print("Sum is :", sum)

tuple = (1)
tuple2 = (1, 2, 3)
for tuple in tuple2:
     print(tuple)
     
dictionary = {"name":"Reagan", "phone": "+254 722 222333"}
print(dictionary)  

def mul(a,b):
    return  a*b
print(mul(4,5))

def multiplication(x,y):
    product = x * y
    return product * product
print(multiplication(2, 3))

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
# Write both numbers to the file
with open('input.txt', 'w') as file:
    file.write(num1 + '\n')
    file.write(num2 + '\n')

# Read the numbers back from the file
with open('input.txt', 'r') as file:
    num1 = file.readline().strip()
    num2 = file.readline().strip()

# Print the values
print("The first number is: " + num1 + " | The second number is: " + num2)


def doubleList(numberList): 
        for number in numberList:
            print(number * 2)
            doubleList([3, 1, 5])