"""
Calculate the bill and tip spread amongst your friends
"""

print("Welcome to the Tip Calculator.")

total: float = float(input("What was the total bill? $"))
tip: int = int(input("What percentage tip would you like to give; 10, 12 or 15? "))
split: int = int(input("How many people to split the bill? "))

tip_percentage:float = tip / 100
total_with_tip: float = total * (1 + tip_percentage)
split_bill: float = round(total_with_tip / split, 2)

print(f"Each person should pay: ${split_bill}")
