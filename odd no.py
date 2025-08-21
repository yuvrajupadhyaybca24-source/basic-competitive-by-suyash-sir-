# Q7: Find the sum of all odd numbers from 1 to A.

N = int(input("Enter a number : "))
i=1
while i <=N:
    if i% 2 !=0:
        print(i)
        i +=1