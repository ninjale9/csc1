class Vending_machines_drinks: 
    def __init__(self,num_soda, num_water, num_coffee) :
        self.num_soda = num_soda
        self.num_water = num_water
        self.num_coffee = num_coffee
    def buy (self,drink):
        Purchase_amount = int(input("Please enter the amount you want: "))
        if drink == "soda":
            if  self.num_soda > 0:
                self.num_soda -= Purchase_amount
            else :
                print("Sorry, no soda left ")
        elif drink == "coffee":
            if  self.num_coffee > 0:
                self.num_coffee -= Purchase_amount
            else :
                print("Sorry, no coffee left")
        elif drink == "water":
            if  self.num_water > 0:
                self.num_water -= Purchase_amount
            else :
                print("Sorry, no water left ")
        else : 
            print ("Invalid drink type ")

    def restock(self,drink_choice, restock_amount):
        drink_choice = drink_choice
        restock_amount = restock_amount
        if drink_choice == 1 : 
            self.num_soda += restock_amount 
        if drink_choice == 2:
            self.num_coffee += restock_amount
        if drink_choice == 3 :
            self.num_water += restock_amount

    def inventory(self ):
        print ("Current inventory: ")
        print(f"Soda: {self.num_soda} bottles")
        print(f"Coffee: {self.num_coffee} bottles")
        print(f"Water : {self.num_water} bottles")

Vending_machine = Vending_machines_drinks(10,10,10)
while True :
    choice = input("Please select what you are doing \n Buy \n restock \n inventory \n when you are done select quit or q \n --> ") .lower()
    if choice == "q" or choice == "quit" : 
        break
    if choice == "buy" : 
        drink_choices = input("Please select between Soda , Coffee, and Water: ")
        Vending_machine.buy(drink_choices)
    if choice == "inventory":
        Vending_machine.inventory()
    if choice == "restock":
        drink_choice = int(input("Please select what option you want to restock\n 1 - Soda\n 2 - Coffee\n 3 - Water:\n -->"))
        restock_amount = int(input("Please enter the amount you want restock to the chosen drink: "))
        Vending_machine.restock(drink_choice,restock_amount)