#printing the welcoming message
print("Welcome to the tip calculator")

#taking the input of bill
bill = int(input("Enter the bill \n"))

#Asking the tip %
tip = int(input("What percent of tip you would like to give? 10,12,15 \n"))

#calculating the tip
tip_calculated = (tip/100)*bill
#printing the total tip
print(f"tip_calculated is {tip_calculated}")

#calculating the total bill including the tip
total_bill = tip_calculated+ bill
#printing the total bill
print(f"total bill is {total_bill}")

#asking the number of people the bill to be splitted
people =int(input("In How many people the bill have to split? \n"))
#calculating each person bill
each_person_bill = total_bill//people
#printing each person bill
print(each_person_bill)
