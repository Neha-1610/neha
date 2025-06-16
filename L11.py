#examples


users = [
  {"id":1 , "name":"Alice" , "age":25},
  {"id":2 , "name":"Melisha" , "age":30}
 ]

while True:
    print("CRUD Operation in python!!")
    print("1. Create user")
    print("2. ead user")
    print("3. update user")
    print("4. delete user")
    print("5. Exit")

    choice = input("Enter your choice(1-5): ")

    if choice == 1:

        try:
            user_id = int(input("Enter id: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            users.append({"id":user_id , })