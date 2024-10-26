tup1= (35, 46, 8, "chipolotes", "hello", True )
tup2=(2,2,3,[3,8,9], "eight")#nesting
print(tup1)
print(tup2[2])
print(tup2[3][1])
sliced=tup2[2:4]
print(sliced)

set1={2,6,4,4,4,6,6,7,7}
print(set1)
set2={"yellow", "turquoise", "amber"}
print(set2)
#add
set2.add("gray")
print(set2)
set3={"blue", "gray", "turquoise", "cyan"}
inter=set2.intersection(set3)
print(inter)
unif=set2.union(set3)
print(unif)
difference=set3.difference(set2)
print(difference)
si=set2.symmetric_difference(set3)
print(si)