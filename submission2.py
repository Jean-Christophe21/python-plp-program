#encoding: utf-8

# create empty list named my_list
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)


# insertion of the value 15 at the second position
my_list.insert(1, 15)

another_list = [50, 60, 70]

# extension of my_list with another list
my_list.extend(another_list)

# sorting my_list in ascending order
my_list.sort()
index = my_list.index(30)
print("Index of 30:", index)
