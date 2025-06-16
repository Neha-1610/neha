#list
#tuples
#set
#dictionary

#list
#mutables

my_list = [1 , 2 , 3]

my_list[1] = 10

my_list.append(20)
my_list.append(20)

del my_list[0]

print(my_list)

#tuple- immutable

my_tuple = (1 , 2 , 3)

#set mutable

my_set = {1, 2, 3}
my_set.add(10)
my_set.add(10)        #duplicate do no support
print(my_set)


#dictionary mutable

my_dics = {"1":"Neha" , "2":"Neha"}

my_dics["1"] = "Yuvraj"

print(my_dics)

# name list

name_list = ["Neha" , "Yuvraj" , "Hitesh"]

for user in name_list:
    print(user)


#type casting constructor
a = [1 , 2 , 3]
b = tuple(a)
c = set(b)

print(a)
print(b)
print(c) 

# dictionary not works becuse it needs 2 characters
