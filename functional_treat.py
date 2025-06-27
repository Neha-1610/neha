print("Welcome to the Data Analyser and Transformer Program\n")

while True:
    
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion) ")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    
    choice = int(input("Enter your choice :"))
    
    if choice == 1:
        print()
        array_input = input("Add Element by seperated space : ")

        arr = list(map(int , array_input.split()))   
        
    elif choice == 2:
        print("Data Summary:  ")    
        print("Total element: " , len(arr))
        print("Minimum value: " , min(arr))
        print("Maximum value: " , max(arr))
        print("Sum of all value: " , sum(arr))
        print("Average value:  " , sum(arr) / len(arr))

    elif choice == 3:
            fact = int(input("Enter a number to Calculate its factorial :"))
            def factorial(n):
                if n == 1:
                    return 1
                else:
                    return n * factorial(n-1)

            print(f"factorial :" , factorial(fact)) 

    elif choice == 4:
        threshold = int(input("Enter a threshold value to filter out data below this value:\n"))
        try:
                print(f"\nFiltered Data (values >= {threshold}):")
                for item in filter(lambda x: x >= threshold, arr):
                    print(item, end=" ")

        except ValueError:
                print("Please enter a valid number.")

    elif choice == 5:
        
        print("\nChoose sorting option:\n1. Ascending\n2. Descending")
        order = int(input("Enter your choice: "))

        if order == 1:
             print("Sorted data in Ascending order: ")
             for x in sorted(arr):
                  print(x, end=(" "))

        elif order == 2:
             print("Sorted data in Descending order: ")
             for x in sorted(arr, reverse=True):
                  print(x, end=(" "))

        else:
             print("Invalid... Please try again")

    elif choice == 6:
         print()
         print("Dataset Statistics:")
         print("Minimum value: " , min(arr))
         print("Maximum value: " , max(arr))
         print("Sum of all values: " , sum(arr))
         print("Average value: " , sum(arr) / len(arr))

    elif choice == 7:
         print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!😎😁😛 ")
         break
    
    else:
         print("Invalid choice.. Please Try Again!!")