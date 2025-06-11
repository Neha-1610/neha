# * pattern in python

for i in range(5):
    print(i)
    for j in range(i):
        print('*' , end=" ")
        print()

# python number pattern

for i in range(6):
 for j in range(i):
   print('*' , end=" ")
print()

# string 
str1 = "Hello"+ "World"
str2 = "Hello" * 10
print(str2)

# pattern 2
for i in range(1 , 6):
   for j in range(i , 0 , -1):
      print(j , end=" ")
      print()
