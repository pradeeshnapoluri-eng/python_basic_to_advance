num=input("Enter list of numbers: ")
num_list=num.split()#split function converts into list.
count=0
for i in num_list:
    count+=1##it adds one to index to convert starting 0 into 1 so we can find length easily
print("The length of the list is",count)
# for i in num_list:##if u want to print in selected numbers
for j in range(count):
    # if int(i)%2==0:###it is totally out of program
    num_list[j]=int(num_list[j])
print("The numbers list is",num_list)
##to find max number;dont use inbuilt function like max().
max_num=num_list[0]##here we put zero because the list index starts from 0
for k in num_list:
    if k > max_num:
        max_num = k
print("The maximum number is",max_num)