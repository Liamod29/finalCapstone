import math
interest=""

#explaining choices
print(" Investment - to calculate the amount of interest you'll earn on your investment\n Bond       - to calculate the amount you'll have to pay on a home loan\n")
#choice of investment or bond
user_choice = input("Please type either Investment or Bond from the menu above to proceed:\n")

#Inputs needed if investment is selected
if user_choice.lower() == "investment":
    deposit = int(input("Please enter your deposit amount:\n"))
    rate = int(input("Please enter your interest rate:\n"))
    no_of_years = int(input("Please enter the number of years you plan to invest:\n"))
    interest = input("Please enter either Simple or Compound to choose interest:\n")


#Inputs needed if bond is selected, and calculation for monthly repayment
elif user_choice.lower() == "bond":
    house_value = int(input("Please enter the value of the house:\n"))
    house_rate = int(input("Please enter the interest rate:\n"))
    months = int(input("Please enter how many months it will take to repay:"))
    repayment= (house_rate / 100 / 12 * house_value)/(1 - (1 +house_rate / 100 / 12)**(-months))
    print("You will have to repay £" + str(round(repayment,2)) + " per month")

else:
    print("Please select a valid choice")

#answer for simple interest on investment
if interest.lower() == "simple":
    answer = deposit*(1+rate/100*no_of_years)
    print("Your amount after "+ str(no_of_years) + " years will be £" + str(round(answer,2)))   

#answer for compound interest on investment
elif interest.lower() == "compound":
    answer2 = deposit *math.pow((1+rate/100),no_of_years)
    print("Your amount after "+ str(no_of_years) + " years will be £" + str(round(answer2,2)))