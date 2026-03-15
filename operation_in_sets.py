# a={1,2,3,4,5,6}
# b={4,5,6,7,8,9}
# c={8,9,10,11,12}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference([1,2,3]))
# print(a.difference(b,c))#it checks 1st set with 2nd set so that difference prints.even the match is there in 3rd set 1st condition accepts.
# print(b.difference(a))
# print(c.difference(b))
# print(a|b)#this is union method
# print(a.union(b,c)) #or simply(b|c)
# print(b.union("girl","boy"))this converts strings into tuples
# print(a.union((9,12,"mohan")))#this adds elements next to selected set.and this cannot pass to '|' operand.
# print(a|(9,12,"mohan"))#this cause error
# print("hello\nworld")#this is just string concatenation...out of sets
# a.update(b)
# a.update([67,89])
# print(a)
# #another operational method is;
# a|=b
# print(a)
# print(a.intersection([00,89])) #it gives set() as output
# # print(a&b)#for intersection
# a.intersection_update(b)
# a.difference_update(b)
# print(a)
# b.difference_update(a)
# print(b)
# print(b)
# print(a-b)
# print(b-a)
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))
# print(a^b)#symmeytry difference operation
# a.symmetric_difference_update(b)#removes the similar elements and join the both element sets in single set
# print(a)
# print(b)
# a.symmetric_difference_update(([67,899]))
# print(a)

#disjoint sets
a={1,2,3,4,5,6,7,8}
b={1,2,3,4,5,6,7,8,9}
# print(a.isdisjoint(b))
# print(a.issubset(b))
# print(a<=b)
# print(a.issuperset(b))
# print(a>=b)
# a.clear()
# b.clear()
# print(a)
# print(b)
del a#here its already deleted
