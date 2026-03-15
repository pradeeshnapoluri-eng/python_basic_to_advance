def prime_num(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime == True:
        print("it is a prime number")
    else:
        print("not a prime number")
num=int(input("enter a number:\n"))
prime_num(num)
print("successfully checked")