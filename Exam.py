while True:

    print("Welcome to the Bill Splitter App!")
    print()
    bill = float(input("Enter the total bill amount:₹" ))
    people= int(input("Enter number of people:"))
    tip = int(input("Enter tip percentage((0 , 5 , 10 , 15 , 20): )"))

    if bill <0 or people <= 0 or tip not in [0 , 5 , 10 , 15 , 20]:
        print("Invalid please try again!")
        continue

    tip = (tip / 100) * bill

    final_bill = bill + tip

    per_person = final_bill / people

    print(f"\nTip amount: ₹{tip:.2f}")
    print(f"total bill (with tip): ₹{final_bill:.2f}")
    print(f"each person should pay: ₹{per_person:.2f}")


    again = input("\nwould you like to calculate another bill? (y/n) ").lower()
    if again != 'y':
        print("Thank you for using the bill splitter app!")
        break