# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:49:25 2017

@author: User
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, \
as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-­annual raise, as a decimal: "))
portion_down_payment = 0.25 
down_payment = portion_down_payment * total_cost
current_savings = 0
monthly_salary = annual_salary / 12
month_num = 1
result = 0
while current_savings < down_payment:
    if month_num % 6 == 1 and month_num > 1:
        monthly_salary = monthly_salary + monthly_salary * semi_annual_raise
    current_savings = current_savings + (portion_saved * (monthly_salary) + \
                                         (current_savings* 0.04/12))
    month_num += 1
    print(current_savings)
print("Number of months: " + str(month_num))