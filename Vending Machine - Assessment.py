#vending Machine
vm_buyitem = []

vm_items = { 'item': 'Water', 'code': '1', 'price': 2.00}
vm_buyitem.append(vm_items)

vm_items = {'item': 'Iced Tea', 'code': '2', 'price': 4.00}
vm_buyitem.append(vm_items)

vm_items = {'item': 'Cola', 'code': '3', 'price': 3.50}
vm_buyitem.append(vm_items)

vm_items = {'item': 'NRG Drink', 'code': '4', 'price': 5.50}
vm_buyitem.append(vm_items)

vm_items = {'item': 'Choco Bar','code': '5', 'price': 5.50}
vm_buyitem.append(vm_items)

vm_items = {'item': 'Biscuits', 'code': '6', 'price': 4.25}
vm_buyitem.append(vm_items)

vm_items = {'item': 'Chips', 'code': '7', 'price': 4.25}
vm_buyitem.append(vm_items)

vm_items = {'item': 'NRG Bar', 'code': '8', 'price': 5.25}
vm_buyitem.append(vm_items)

def vm_mmenu ():
    print ("Welcome to the vending machine (powered by Python!).")
    print ("Here are the available items in the vending machine:\n")

    for i in vm_buyitem:
        print ("==============================================")
        print (f"== Item: {i['item']} - Code: {i['code']} - Price: {i['price']} ==")
vm_mmenu ()

water= 2.00
ice_tea = 4.00
cola = 3.50
nrg_drink = 5.50
choco_bar = 5.50
biscuits = 4.25
chips = 4.25
nrg_bar = 5.25
vm_credits = 0

vm_credits = float (input("\nEnter the amount of money you will put in: "))
if vm_credits <= 0:
    print ("You have placed a insufficient amount of credits. Please try again.")
    exit()

vm_item = input("Select the item that you will buy: ")

if vm_item == '1':
    print("\nYou have selected the water. The item costs 2 dhs.")
    if vm_credits < water:
            print("Sorry, you don't have enough cash for the product")
            exit()
    elif vm_credits >= water:
            vm_credits -= water
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying water, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    \tYou have purchased water.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()

        
if vm_item == '2':
    print("\nYou have selected the iced tea. The item costs 4 dhs.")
    if vm_credits < ice_tea:
            print("\nSorry, you don't have enough credits for this item.")
            exit()
    elif vm_credits >= ice_tea:
            vm_credits -= ice_tea
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying iced tea, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    \tYou have purchased iced tea.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()

if vm_item == '3':
    print("\nYou have selected the cola. The item costs 3 dhs.")
    if vm_credits < cola:
            print("\nSorry, you don't have enough credits for this item.")
            exit()
    elif vm_credits >= cola:
            vm_credits -= cola
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying cola, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    \tYou have purchased cola.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()

if vm_item == '4':
    print("\nYou have selected the energy drink. The item costs 5 dhs.")
    if vm_credits < nrg_drink:
            print("\nSorry, you don't have enough credits for this item.")
            exit()
    elif vm_credits >= nrg_drink:
            vm_credits -= nrg_drink
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying the energy drink, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    \tYou have purchased energy drink.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()

if vm_item == '5':
    print("\nYou have selected the chocolate bar. The item costs 5 dhs.") 
    if vm_credits < choco_bar:
            print("\nSorry, you don't have enough credits for this item.")
            exit()
    elif vm_credits >= choco_bar:
            vm_credits -= choco_bar
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying the chocolate bar, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    You have purchased chocolate bar.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()

if vm_item == '6':
    print("\nYou have selected the biscuits. The item costs 4 dhs.") 
    if vm_credits < biscuits:
            print("\nSorry, you don't have enough credits for this item.")
            exit()
    elif vm_credits >= biscuits:
            vm_credits -= biscuits
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying biscuits, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    \tYou have purchased biscuits.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()

if vm_item == '7':
    print("\nYou have selected the chips. The item costs 4 dhs.") 
    if vm_credits < chips:
            print("\nSorry, you don't have enough credits for this item.")
            exit()
    elif vm_credits >= chips:
            vm_credits -= chips
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying chips, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    \tYou have purchased chips.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()

if vm_item == '8':
    print("\nYou have selected the energy bar. The item costs 5 dhs.")
    if vm_credits < nrg_bar:
            print("\nSorry, you don't have enough credits for this item.")
            exit()
    elif vm_credits >= nrg_bar:
            vm_credits -= nrg_bar
            print ("\nYour item and your change has been dispensed.")
            print ("\nYour change is " + str(vm_credits) + " dhs. Thank you for buying the energy bar, have a nice day!")

            receipt = input ("Would you like to print a receipt? (Enter 'print' to print / Press 'enter' to skip): ")
            if receipt == 'print':
                    print (f"""
                    ==================================
                    Reciept == Python Vending Machine
                    \tYou have purchased energy bar.
                
                    \tChange = {str(vm_credits)}.
                    ==================================
                    """)
            else: 
                print ("Thank you for buying!")
                exit ()