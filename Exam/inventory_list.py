inventory = []
print("\nWelcome to Inventory List Analyzer!\n")

items = { }
categories = [ ]

while True:
    name = input("Enter item name: ").lower
    category = input("Enter category: ").lower
    quantity = int(input("Enter quantity: "))

    items[name] = quantity

    inventory.append({
        "name": name,
        "category": category,
        "quantity": quantity
    })

    add = input("Do you want to add more items? (y/n): ")
    if add.lower() != 'y':
        break
print()

print("========== INVENTORY SUMMARY ==========")

print("Total Different Items: " , len(items))

print("Total Quantity in Stock: " , sum(items.values()))

avg = sum(items.values())/ len(items)
print("Average Quantity per Item: " ,avg)

max = max(items, key=items.get)
min = min(items, key=items.get)
print("Most Stocked Item: " , max ,  "-", items[max], "units")
print("Least Stocked Item: " , min ,  "-", items[min], "units")
print()

categories = sorted(set(item['category'] for item in inventory))
print("\n----------------------------------------\n")
print(f"Unique Categories in Inventory: {set(categories)}")

print("\n----------------------------------------\n")

print("Items Sorted by Quantity (High to Low):")
sorted_items = sorted(inventory, key=lambda x: x['quantity'], reverse=True)
for i, item in enumerate(sorted_items, start=1):
    print(f"{i}. {item['name']} - {item['quantity']} units")

print("\n----------------------------------------\n")

print("Categories in Alphabetical Order:")
for i, category in enumerate(categories, start=1):
    print(f"{i}. {category}")