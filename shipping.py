weight = 8.4
price = 0
premium_ground = 125
#ground shipping
if weight <= 2:
  price = 1.5 * weight + 20 + premium_ground
  print("It will cost $" + str(price) + " to ship this box")
elif weight <= 6:
  price = 3 * weight + 20 + premium_ground
  print("It will cost $" + str(price) + " to ship this box")
elif weight <= 10:
  price = 4 * weight + 20 + premium_ground
  print("It will cost $" + str(price) + " to ship this box")
else:
  price = 4.75 * weight + 20 + premium_ground
  print("It will cost $" + str(price) + " to ship this box")
#drone shipping
weight = 1.5
price = 0
if weight <= 2:
  price = 4.5 * weight 
  print("It will cost $" + str(price) + " to ship this box")
elif weight <= 6:
  price = 9 * weight 
  print("It will cost $" + str(price) + " to ship this box")
elif weight <= 10:
  price = 12 * weight 
  print("It will cost $" + str(price) + " to ship this box")
else:
  price = 14.25 * weight 
  print("It will cost $" + str(price) + " to ship this box")
