"""
This program provides a suggestion to name your new band!
"""

print("Welcome to the Band Name Generator")

city: str = str(input("What is the name of the city you grew up in?\n"))
pet: str = str(input("What is the name of your pet?\n"))

band_name: str = city + " " + pet
print("Your band name could be " + band_name)
