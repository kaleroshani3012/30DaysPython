print("\n********************************* Program Started *********************************")
Inventory = {}

while True:
    print("\nWelcome to Rohan Provision Store")
    print("""
            1. Add Items
            2. Search Item
            3. Update Item Price and Quantity
            4. Delete Item
            5. View Items
            6. Exit
         """)
    
    ch = int(input("Enter Your Choice: "))

    if ch>=1 and ch<=5:
        if ch == 1:
            item = input("\nEnter Product Name: ").strip().lower().capitalize()
            if item in Inventory:
                print("\nProduct Already Available, Still you can Update Price and Quantity")
                ans1 = input("\nYou want to update item price (yes/no) ").strip().lower()
                if ans1 == "yes":
                    print(f"\ncurrent details: Price = {Inventory[item]['Price']} ")
                    new_price = float(input("\nEnter Price to Update: "))
                    Inventory[item]["Price"] = new_price
                    print(f"updated details: {item} Price = {Inventory[item]['Price']} ")

                ans2 = input("\nYou want to update item quantity(yes/no) ").strip().lower()
                if ans2 == "yes":
                    print(f"\ncurrent details: Quantity = {Inventory[item]['Quantity']}")
                    new_qty = int(input("\nEnter Quantity to Update: "))
                    Inventory[item]["Quantity"] = new_qty
                    print(f"updated details: {item} Quantity = {Inventory[item]['Quantity']} ")
            
                if ans1 != "yes" and ans2 != "yes":
                    print("No changes made!!!")

            else:
                price = float(input("Enter Product Price: "))
                qty = int(input("Enter Product Quantity: "))

                Inventory[item] = {"Price" : price, "Quantity" : qty}
                print(f"\n{item.capitalize()} Added to Inventory")

        elif ch == 2:
            item_to_search = input("\nEnter Item Name to Search Details: ").strip().lower().capitalize()
            if item_to_search in Inventory:
                print(f"\nYay, Searched Item Found: {item_to_search}")
                print(f"-> Price:    {Inventory[item_to_search]['Price']}")
                print(f"-> Quantity: {Inventory[item_to_search]['Quantity']}")

            else:
                print(f"\n{item_to_search} is Not Available in Inventory")


        elif ch == 3:
            item1 = input("\nWhich Item you want to Update: ").strip().lower().capitalize()
            if item1 in Inventory:    
                ans1 = input("\nYou want to update item price(yes/no) ").strip().lower()
                if ans1 == "yes":
                    print(f"\ncurrent details: Price = {Inventory[item1]['Price']} ")
                    new_price = float(input("\nEnter Price to Update: "))
                    Inventory[item1]["Price"] = new_price
                    print(f"updated details: {item1} Price = {Inventory[item1]['Price']} ")

                ans2 = input("\nYou want to update item quantity(yes/no) ").strip().lower()
                if ans2 == "yes":
                    print(f"\ncurrent details: Quantity = {Inventory[item1]['Quantity']}")
                    new_qty = int(input("\nEnter Quantity to Update: "))
                    Inventory[item1]["Quantity"] = new_qty
                    print(f"updated details: {item1} Quantity = {Inventory[item1]['Quantity']} ")
                
                if ans1 != "yes" and ans2 != "yes":
                        print("No changes made!!!")
            
            else:
                print("Item not Found, Enter 1 to add Product in Inventory")

        elif ch == 4:
            item = input("\nEnter item to Delete from Inventory: ").capitalize()
            if item not in Inventory:
                print("\nSorry ! Item not present in inventory to Delete")
            else:
                del Inventory[item]
                print(f"\nHurrey, {item} Deleted from Inventory")

            if not Inventory:
                print("\nThere is No Item Available in Inventory")
            else:
                for item_name,details in Inventory.items():
                    print(f"\n{item_name} : Price = {details['Price']}, Quantity = {details['Quantity']}")


        
        elif ch == 5:
            if not Inventory:
                print("Inventory is Empty")

            else:
                print("\n************* Current Available Products *************\n")
                for item,details in Inventory.items():
                    print(f"{item} : Price = {details['Price']}, Quantity = {details['Quantity']}")
        
    else:
        print("\n********************************* End of Programme *********************************")
        break

            

