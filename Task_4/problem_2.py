n = int(input())
students = []
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

grades = sorted(set(g for _, g in students))
second_lowest = grades[1]

result = sorted([name for name, grade in students if grade == second_lowest])
for name in result:
    print(name)
