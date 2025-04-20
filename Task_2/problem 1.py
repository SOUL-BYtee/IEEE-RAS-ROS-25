numbers = []
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    numbers.append(num)

if numbers:
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
else:
    print("No numbers entered.")