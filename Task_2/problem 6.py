num = int(input("Enter a positive integer: "))
even_sum = sum(i for i in range(1, num + 1) if i % 2 == 0)
print(f"The sum of even numbers from 1 to {num} is {even_sum}")
