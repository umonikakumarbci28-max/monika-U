my_list=[1,2,3,4,5,7,6,8,9,9]
new_set=(set(my_list))
my_list1=[7,14,21,28,35,49]
new_set1=(set(my_list1))
new_set2=new_set.intersection(new_set1)
print(list(new_set2))



