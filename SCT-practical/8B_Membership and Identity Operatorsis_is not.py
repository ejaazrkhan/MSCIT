my_new_list1 = [1, 2, 3, 'a']
my_new_list2 = my_new_list1
my_new_tuple1 = (1, 2, 3, 'a')
my_new_tuple2 = (4, 5, 'b', 'a')

print("my_new_list1", my_new_list1)
print("type of my_new_list1",type(my_new_list1))

print("my_new_list2", my_new_list2)
print("type of my_new_list2",type(my_new_list2))

print("my_new_tuple1", my_new_tuple1)
print("type of my_new_tuple1", type(my_new_tuple1))

print("my_new_tuple2", my_new_tuple2)
print("type of my_new_tuple2", type(my_new_tuple2))

if type(my_new_list1) is not type(my_new_tuple1):
    print('true!!! ,my_new_list1 &  my_new_tuple1 does not belong to same type')
else:
    print("my_new_list1 &  my_new_tuple1 belong to same type")

if type(my_new_tuple1) is not type(my_new_tuple2):
    print('true!!!, my_new_tuple1 & my_new_tuple2 does not belong to same type')
else:
    print("my_new_tuple1 & my_new_tuple2 belong to same type")

if (my_new_list1) is not (my_new_list2):
    print("true!!!, my_new_list1 & my_new_list2 are not same")
else:
    print("my_new_list1 & my_new_list2 are same")
