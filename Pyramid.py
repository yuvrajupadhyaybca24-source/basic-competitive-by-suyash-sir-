# N=int(input())
# for i in range(1,N+1):
#     for j in range(N-i+1):
#         print("*",end=" ")
#     for j in range(2*i-2):
#         print(" ",end=" ")
#     for j in range(N-i+1):
#         print("*",end=" ")
#     print()



N=int(input())
for i in range(1,N+1):
    for j in range(i):
        print("*",end=" ")
    for j in range(2*N-2*i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()