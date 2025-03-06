#Name:
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class store:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def cost_2_percent_increase(self):
        self.cost *= (2)

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
flour = store(20, 4, 6)
eggs = store(13, 6, 1)
bread = store(20, 5, 1)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"The stock of flour: {flour.stock}")
print(f"The stock of eggs: {eggs.stock}")
print(f"The stock of bread: {bread.stock}")
print(f"The cost of eggs: {eggs.cost}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
eggs.cost_2_percent_increase()
print(f"The new cost of eggs: {eggs.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
bread.stock = 5
print(f"The new stock of bread: {bread.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del flour

try:
    print(f"The weight of flour: {flour.weight}")
except NameError:
    print("sold out until thursday")