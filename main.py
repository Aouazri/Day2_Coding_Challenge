#Creating a tip calculator to see how much each person should pay 
print("Welcome to the tip Calculator.")
bill = float(input("What was the total bill? $"))
tip =int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_price = bill * (1+ tip/100)
#Rounding the price to two decimal places.
bill_per_person= round((total_price / people), 2)
final_amount= "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
