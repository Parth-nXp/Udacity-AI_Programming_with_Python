class Shirt:
    # Constructor method to initialize Shirt object with color, size, style, and price
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        # Assigning values to instance variables
        self.color = shirt_color  # Shirt color
        self.size = shirt_size    # Shirt size
        self.style = shirt_style  # Shirt style
        self.price = shirt_price  # Shirt price

    # Method to change the price of the shirt
    def change_price(self, new_price):
        self.price = new_price  # Update the price with the new value

    # Method to calculate the discounted price of the shirt
    def discount(self, discount):
        return self.price * (1 - discount)  # Calculate discounted price

# End of the class definition

# defining the new object
new_shirt = Shirt('red','S','short sleeve', 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)


new_shirt.change_price(10)
print(new_shirt.price)

new_shirt.discount(0.2)
print(new_shirt.price)

tshirt_collection = []

shirt_one = Shirt('orange','M','short sleeve', 25)
shirt_two = Shirt('red','S','short sleeve',15)
shirt_three = Shirt('purple','XL','short sleeve',10)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)
print(tshirt_collection)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)