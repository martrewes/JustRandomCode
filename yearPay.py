#!/usr/bin/python

import decimal
from decimal import Decimal

hourly = input("Enter Hourly Wage: ")
hours = input("Enter Hours per Week: ")

weekly = Decimal(hours) * Decimal(hourly)
yearly = weekly * 52
monthly = yearly / 12

# results
print("")

print("####################################")
print("# ______                _ _        #")
print("# | ___ \              | | |       #")
print("# | |_/ /___  ___ _   _| | |_ ___  #")
print("# |    // _ \/ __| | | | | __/ __| #")
print("# | |\ \  __/\__ \ |_| | | |_\__ \ #")
print("# \_| \_\___||___/\__,_|_|\__|___/ #")
print("# 				  #")
print("####################################")                               
print("# Weekly Wage:  £" + str(round(weekly, 2)))
print("####################################")
print("# Monthly Wage: £" + str(round(monthly, 2)))
print("####################################")
print("# Yearly Wage:  £" + str(round(yearly, 2)))
