"""
CP1404/CP5632 - Practical
Shop calculator with discount threshold
"""


total_price = 0
discount_threshold = 100

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > discount_threshold:
    total_price = total_price - (total_price * 0.1)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
