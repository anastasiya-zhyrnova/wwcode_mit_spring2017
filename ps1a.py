# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 23:01:06 2017

@author: User
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, \
as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25 
down_payment = portion_down_payment * total_cost
current_savings = 0
monthly_salary = annual_salary / 12
result = 0
while current_savings < down_payment:
    current_savings = current_savings + (portion_saved * (monthly_salary) + \
                                         (current_savings* 0.04/12))
    result += 1
print("Number of months: " + str(result))
 
