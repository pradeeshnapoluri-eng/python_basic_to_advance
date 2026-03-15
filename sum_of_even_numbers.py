# total=0
# for i in range(0,10):
#     total += 9
#     print(total)
# print("the tables are",total)
### used to find tables (created by me)

total = 0
for i in range(1,101):
    if i % 2 == 0:
        # total += 2 ##this is used to find even numbers between 1 to 100
        total += i ##this is used to find even numbers
        print(total)
print("the total is:",total)