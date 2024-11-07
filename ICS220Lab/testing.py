#testing.py
from classes import EBook, EBookStore, SpecialEditionEBook, Customer, ShoppingCart, Order, Invoice, Payment

# Constants for Discounts and VAT
LOYALTY_DISCOUNT = 0.10  # 10% loyalty discount
BULK_DISCOUNT = 0.20  # 20% discount for bulk purchase
VAT_RATE = 0.08  # 8% VAT

# Create some e-books
ebook1 = EBook("Python Programming", "Mahra Khaled", "2022-03-01", "Programming", 29.99)
ebook2 = EBook("Machine Learning 101", "Salama Ali", "2021-05-15", "Technology", 19.99)
special_ebook = SpecialEditionEBook("Advanced AI", "Dr. Moh", "2023-01-20", "AI", 49.99, "Exclusive Chapter", True)

# Create an e-book store and add e-books
store = EBookStore("Tech Books Store")
store.add_ebook(ebook1)
store.add_ebook(ebook2)
store.add_ebook(special_ebook)

# Create a customer
customer1 = Customer("Alyazia Saeed", "alyazia@email.com", True)  # Loyalty member
customer2 = Customer("Mariam Abdulla", "mariam@email.com", False)  # Non-loyalty member

# Register customers to the store
store.register_customer(customer1)
store.register_customer(customer2)

# Create shopping carts and add items to them
cart1 = ShoppingCart()
cart1.add_item(ebook1)
cart1.add_item(ebook2)

cart2 = ShoppingCart()
cart2.add_item(special_ebook)

cart3 = ShoppingCart()  # Bulk order
cart3.add_item(ebook1)
cart3.add_item(ebook2)
cart3.add_item(special_ebook)
cart3.add_item(ebook1)
cart3.add_item(ebook2)

# Create orders for customers
order1 = Order(101, "2024-11-07", customer1, cart1)  # Loyalty member order
order2 = Order(102, "2024-11-07", customer2, cart2)  # Non-loyalty member order
order3 = Order(103, "2024-11-07", customer1, cart3)  # Bulk order

# Calculate the final price, apply discounts, and finalize the orders
order1.calculate_final_price()
order1.apply_loyalty_discount()  # Apply loyalty discount for customer1
order2.calculate_final_price()  # For non-loyalty customers, no discount applied
order3.calculate_final_price()
order3.apply_bulk_discount()  # Apply bulk discount for cart3

# Create invoices for each order
invoice1 = Invoice(1001, [ebook1.get_title(), ebook2.get_title()], 49.98, 5.00, order1.get_discount(), order1.get_final_price())
invoice2 = Invoice(1002, [special_ebook.get_title()], 49.99, 5.00, order2.get_discount(), order2.get_final_price())
invoice3 = Invoice(1003, [ebook1.get_title(), ebook2.get_title(), special_ebook.get_title(), ebook1.get_title(), ebook2.get_title()], 149.95, 10.00, order3.get_discount(), order3.get_final_price())

# Update invoices based on order details
invoice1.update_invoice(order1)
invoice2.update_invoice(order2)
invoice3.update_invoice(order3)

# Create payment instances for each order
payment1 = Payment(2001, order1, "Credit Card", order1.get_final_price(), "2024-11-07")
payment2 = Payment(2002, order2, "Paypal", order2.get_final_price(), "2024-11-07")
payment3 = Payment(2003, order3, "Credit Card", order3.get_final_price(), "2024-11-07")

# Validate payments
print(f"Payment for Order 101 is {'valid' if payment1.validate_payment() else 'invalid'}")
print(f"Payment for Order 102 is {'valid' if payment2.validate_payment() else 'invalid'}")
print(f"Payment for Order 103 is {'valid' if payment3.validate_payment() else 'invalid'}")

# Display invoice details
print("----- Invoice 1 -----")
invoice1.display_invoice()
print("----- Invoice 2 -----")
invoice2.display_invoice()
print("----- Invoice 3 -----")
invoice3.display_invoice()

# Print store details
print("----- Store Details -----")
print(store)

# Print order details
print("----- Order Details -----")
print(order1)
print(order2)
print(order3)

# Print customer details
print("----- Customer Details -----")
print(customer1)
print(customer2)