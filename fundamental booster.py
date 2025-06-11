def personal_data_collector():

 print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters:" ))
favno = int(input("Please enter your favourite number:"))

print("Thank you! Here is the information we collected:")
print(f"Name: {name} (Type: {type(name)} , Memory Address: {id(name)})")
print(f"Name: {age} (Type: {type(age)} , Memory Address: {id(age)})")
print(f"Name: {height} (Type: {type(age)} , Memory Address: {id(age)})")
print(f"Name: {favno} (Type: {type(favno)} , Memory Address: {id(favno)})")

birthyear = 2025 - age
print(f"Your birth year is approximately: {birthyear} (based on your age of {age})")
print(f"Favourite Number: {favno} (type{favno}), Memory address: {id(favno)}")
print("Thank you for using the Personal Data Collector, Goodbye!")

personal_data_collector()