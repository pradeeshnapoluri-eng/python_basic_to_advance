# ##solid square pattern
# for i in range(5): ## outer loop=rows
#     for j in range(7): ##innerloop=columns
#         print("*",end=" ")
#     print()
# print("this loop is completed successfully")
# ##left half pyramid
# for i in range(1,7):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# print("this loop is completed successfully")
# ##left half pyramid(with numbers)
# for i in range(1,7):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# print("this loop is completed successfully")
# ##left half pyramid(with increasing numbers)
# for i in range(1,7):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print("this loop is completed successfully")
# ##inverted left half pyramid
# row=6
# for i in range(1,row+1):
#     for j in range(1,row-i+1):
#         print("*",end=" ")
#     print()
# print("this loop is completed successfully")
# ##inverted left half pyramid(number)
# row=6
# for i in range(1,row+1):
#     for j in range(1,row-i+1):
#         print(i,end=" ")
#     print()
# print("this loop is completed successfully")
# ##inverted left half pyramid with increasing numbers
# row=6
# for i in range(1,row+1):
#     for j in range(1,row-i+1):
#         print(j,end=" ")
#     print()
# print("this loop is completed successfully")
# ##full pyramid
# num=8
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()
# print("this loop is completed successfully")
# ##inverted full pyramid
# num=8
# for i in range(num):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(2*(num-i)-1):
#         print("*",end=" ")
#     print()
# print("this loop is completed successfully")
##diamond pattern
# num=8
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(2* i+1):
#         print("*",end=" ")
#     print()
# for i in range(num-2,-1,-1):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()
# print("this loop is completed successfully")
##vertical half diamond
# n=9
# mid=n//2
# for i in range(n):
#     if i<=mid:
#         stars=i+1
#     else:
#         stars=n-i
#     for j in range(stars):
#         print("*",end=" ")
#     print()
# print("this loop is completed successfully")
##hollow square pattern
# n=6
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# print("this loop is completed successfully")
##hollow right triangle
# n=6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==i or i==n:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
# print("the loop is completed successfully")
##
