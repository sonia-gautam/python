print("Welcome to Sonia's Python Groceries!")
inumber = int(input("How many items do you have?"))
times = 1
total = 0
while inumber >= times:
    item = str(input("What is the name of your item?"))
    qty = int(input("How many of these are you buying?"))
    price = float(input("What is the price of your item?"))
    total = total + float(qty * price)
    times = times + 1
tax = float(total * .0975)
print("Tax: $" ,tax)
tt = tax + total
print("Total plus tax: $" ,tt)
print("Thank you for shopping:)")
