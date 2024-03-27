cents = int(input("Please enter the cents you need to convert: "))
quarter_value = 25
dime_value = 10
nickel_value = 5
penny_value = 1

quarters = cents // quarter_value
quarters_left = cents % quarter_value
dimes = quarters_left // dime_value
dimes_left = quarters_left % dime_value
nickels = dimes_left // nickel_value
nickels_left = dimes_left % nickel_value
pennies = nickels_left // penny_value

# Display the results
print(f'Coins: Quarters:{quarters} Dimes:{dimes} Nickels:{nickels} Pennies:{pennies}')