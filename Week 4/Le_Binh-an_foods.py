food_dict= {
    "Hot Dog" : 1.50 ,
    "Slice of Pizza" : 1.99, 
    "Whole Pizza" : 9.95,
    "Soft Drink" : 0.59 
}
hot_dog= int(input("Please enter the number of hot dog you want: "))
slice_of_pizza = int(input("Please enter the number of slices of pizza you want: "))
whole_pizza = int(input("Please enter the number of whole pizza you want: "))
soft_drink = int(input("Please enter the number of soft drinks you want: "))

hot_dog= food_dict["Hot Dog"] * hot_dog
slice_of_pizza = food_dict["Slice of Pizza"] * slice_of_pizza 
whole_pizza = food_dict['Whole Pizza'] * whole_pizza
soft_drink = food_dict["Soft Drink"] * soft_drink 

Total_cost = hot_dog + slice_of_pizza + whole_pizza + soft_drink

print (f'your total cost comes out to be {Total_cost:.2f}')