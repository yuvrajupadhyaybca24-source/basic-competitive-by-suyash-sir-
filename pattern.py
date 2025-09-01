N= int(input("Enter a Number:"))
for i in range(1,N+1):
    for j in range(1,i+1):
        if(j%2==0):
             print("*",end=" ")
        else:
            print(j,end=" ")
    print()





# N=int(input())
# for i in range(1,N+1):
#     for j in range(1,N+1):
#        if(j==1 or j==N):
#             # print("*",end=" ")           //// three space*
#        else:
#            print("_",end=" ")
#     print()


# N=int(input())
# for i in range(1,N+1):
#     for j in range(N-i):
#         print("*",end=" ")       ///////// straight 5 *
#     for j in range(i):
#         print("*",end=" ")
#     print()

