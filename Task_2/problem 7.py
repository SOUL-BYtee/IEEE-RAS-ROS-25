num = int(input("Enter a positive integer: "))
i = 2
factors = []
while num > 1:
    while num % i == 0:
        factors.append(i)
        num //= i
    i += 1

print("Prime Factors:", ", ".join(map(str, factors)))