#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("**** WELCOME TO THE TIP CALCULATOR ****")
original_bill = float(input("Enter the total bill : $"))
tip_percent = float(input("Enter the percentage tip you would like to give (10,12 or 15) : "))
people_count = int(input("Enter the no. of people to split the bill : "))

total_bill = (original_bill) + (original_bill * (tip_percent/100))

bill_split = round(total_bill/people_count, 2)

print(f"Each person should pay ${bill_split}.")
