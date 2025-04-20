num = int(input("Enter a positive integer: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"The factorial of {num} is {fact}")