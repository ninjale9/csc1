principle = int(input("Enter the loan principle:"))
month = int(input("Enter the loan term in months:"))
rate = float(input("Enter the annual interest rate of the loan in decimal:"))
Amount= principle*(1+rate/12)**month-principle
print('Your amount of interest in this loan is', Amount)