# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Each product is a tuple: (product_id, name, price, quantity, category)
product1 = ("P001", "Smartphone X", 799.99, 10, "Mobile Phones")
product2 = ("P002", "Laptop Pro", 1199.99, 5, "Laptops")
product3 = ("P003", "Wireless Headphones", 199.99, 15, "Audio")
product4 = ("P004", "Smartwatch Z", 349.99, 3, "Wearables")
product5 = ("P005", "Gaming Laptop", 1499.99, 2, "Laptops")

# TODO 2: Create an inventory list containing all product tuples
inventory = [product1, product2, product3, product4, product5]

# TODO 3: Display all products
print("\nCurrent Inventory:")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 4: Access specific elements
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price, second_quantity = inventory[1][2], inventory[1][3]

print("\n\nAccessing Specific Products:")
print("-" * 60)
print("First product:", first_product)
print("Last product:", last_product)
print("Third product name:", third_product_name)
print("Second product price:", second_price)
print("Second product quantity:", second_quantity)

# TODO 5: Use slicing to get subsets
first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]

print("\n\nProduct Subsets Using Slicing:")
print("-" * 60)
print("First three products:", first_three)
print("Products from index 2 to 4:", middle_products)
print("All except first product:", all_except_first)

# TODO 6: Add new products to inventory
product6 = ("P006", "Tablet A", 499.99, 8, "Tablets")
product7 = ("P007", "Bluetooth Speaker", 149.99, 12, "Audio")
inventory.append(product6)
inventory.append(product7)

print("\n\nAdding New Products:")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 7: Remove a product
removed_product = inventory.pop(2)  # Remove third product (index 2)
print("\n\nRemoving a Product:")
print("-" * 60)
print("Removed product:", removed_product)
print("Updated inventory:")
for product in inventory:
    print(product)

# TODO 8: Insert a product at a specific position
product8 = ("P008", "Fitness Tracker", 129.99, 7, "Wearables")
inventory.insert(1, product8)

print("\n\nInserting a Product:")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 8.1: Redo TODO 4 and 5 after modifications
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price, second_quantity = inventory[1][2], inventory[1][3]

first_three = inventory[:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]