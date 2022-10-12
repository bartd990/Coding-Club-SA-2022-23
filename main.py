#ask for total price
total_cost = int(
  input("What's the total cost of the house? (Please no commas): "))

#calculate down payment and set savings to 0 and set r
portion_down_payment = total_cost / 4
current_savings = 0
r = 0.04

#ask salary and calculate monthly
annual_salary = int(
  input(
    "What's your current annual salary? Please do not include bonuses, and please write the full amount (no commas).: "
  ))
monthly_salary = annual_salary / 12

#ask save %
portion_save = float(
  input(
    "What percentage do you wish to save? Please put it as decimal form. I.E. 100% equals 1"
  ))

#find investments
annual_return = current_savings * r / 12

annual_return = 