a=int(input("Enter a number: "))
for i in range(1,11):
    count = 0
print(a)
while a>100:
    count += 1
    print(i)
    print(count)
    if a<=9:
        print("single")
        break
    elif a>=10 and a<=99:
        print("double")
        break
        # continue
    elif a==100:
        print("century")
        break
    else:
        print("error")
print("end")
