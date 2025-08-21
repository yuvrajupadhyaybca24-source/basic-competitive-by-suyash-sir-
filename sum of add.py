
A = int(input("Enter a positive integer A: "))
Total = 0
i = 1
while i <= A:
    if i % 2 == 0:
        total+= i
    i += 1
print(total)