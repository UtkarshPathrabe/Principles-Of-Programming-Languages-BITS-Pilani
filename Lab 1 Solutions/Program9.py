num1, num2 = input("Enter any two numbers: ").split()

def swap(a, b):
    a ,b = b, a
    return (a, b)

num1, num2 = swap(num1, num2)
print("The numbers after swapping are: "+ num1 +" & " + num2)
