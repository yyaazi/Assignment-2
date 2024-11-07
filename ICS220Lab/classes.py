# classes.py

# EBook class represents an e-book in the store, containing attributes like title, author, etc.
class EBook:
    """Represents an e-book in the store."""
    def __init__(self, title, author, publication_date, genre, price):
        # Initialize the e-book's attributes
        self._title = title # Private attribute
        self._author = author # Protected attribute
        self._publication_date = publication_date
        self._genre = genre
        self._price = price

    def get_title(self):
        # Return the title of the e-book
        return self._title

    def set_title(self, title):
        # Set a new title for the e-book
        self._title = title

    def __str__(self):
        # Return a string representation of the e-book
        return f"EBook(title={self._title}, author={self._author}, genre={self._genre}, price={self._price})"


# EBookStore class represents the store that manages the e-books and customer accounts.
class EBookStore:
    """Represents the e-book store which manages e-books and customer data."""
    def __init__(self, name):
        # Initialize store's name and empty lists for e-books and customers
        self._name = name
        self._eBooksList = []  # List of EBook objects
        self._customersList = []  # List of Customer objects

    def get_name(self):
        # Get the name of the e-book store
        return self._name

    def set_name(self, name):
        # Set a new name for the e-book store
        self._name = name

    def get_eBooks_list(self):
        # Get the list of all e-books in the store
        return self._eBooksList

    def set_eBooks_list(self, eBooksList):
        # Set a new list of e-books for the store
        self._eBooksList = eBooksList

    def get_customers_list(self):
        # Get the list of all customers
        return self._customersList

    def set_customers_list(self, customersList):
        # Set a new list of customers for the store
        self._customersList = customersList

    def add_ebook(self, ebook):
        # Add a new e-book to the store's list
        self._eBooksList.append(ebook)

    def remove_ebook(self, ebook_id):
        # Remove an e-book from the store by matching its title
        self._eBooksList = [ebook for ebook in self._eBooksList if ebook._title != ebook_id]

    def register_customer(self, customer):
        # Register a new customer to the store
        self._customersList.append(customer)

    def __str__(self):
        # Return a string representation of the store, showing name, e-books, and customers
        return f"EBookStore(name={self._name}, eBooksList={self._eBooksList}, customersList={self._customersList})"


# SpecialEditionEBook class is a subclass of EBook that represents special edition e-books.
class SpecialEditionEBook(EBook):
    """Represents a special edition of an e-book."""
    def __init__(self, title, author, publication_date, genre, price, special_features, limited_edition):
        # Initialize attributes for special edition e-books, including unique features
        super().__init__(title, author, publication_date, genre, price)
        self._special_features = special_features
        self._limited_edition = limited_edition

    def __str__(self):
        # Return a string representation of the special edition e-book
        return f"SpecialEditionEBook({super().__str__()}, features={self._special_features}, limited_edition={self._limited_edition})"


# Customer class represents a customer in the e-book store.
class Customer:
    """Represents a customer of the e-book store."""
    def __init__(self, name, contact_info, is_loyalty_member=False):
        # Initialize customer's basic details and loyalty status
        self._name = name
        self._contact_info = contact_info
        self._is_loyalty_member = is_loyalty_member
        self._orderList = []  # List of orders placed by the customer

    @property
    def is_loyalty_member(self):
        # Property to get the loyalty status of the customer
        return self._is_loyalty_member

    @is_loyalty_member.setter
    def is_loyalty_member(self, value):
        # Setter to change loyalty status, if necessary
        if isinstance(value, bool):
            self._is_loyalty_member = value
        else:
            raise ValueError("Loyalty status must be a boolean value.")

    def place_order(self, order):
        # Add an order to the customer's order list
        self._orderList.append(order)

    def __str__(self):
        # Return a string representation of the customer, showing their name and loyalty status
        return f"Customer(name={self._name}, loyal={self._is_loyalty_member})"


# ShoppingCart class represents a customer's shopping cart.
class ShoppingCart:
    """Represents a shopping cart for holding e-books."""
    def __init__(self):
        # Initialize an empty list of items in the cart
        self._itemsList = []

    def add_item(self, ebook):
        # Add an e-book to the shopping cart
        self._itemsList.append(ebook)

    def __str__(self):
        # Return a string representation of the shopping cart and its items
        return f"ShoppingCart(items={self._itemsList})"


# Order class represents an order placed by a customer for e-books.
class Order:
    """Represents an order placed by a customer."""
    def __init__(self, order_id, order_date, customer, shopping_cart):
        # Initialize order details including order ID, date, customer, and shopping cart
        self._order_id = order_id
        self._order_date = order_date
        self._customer = customer
        self._shopping_cart = shopping_cart
        self._invoice = None  # Invoice for this order, to be generated later
        self._discount_amount = 0.0  # Discount applied to the order
        self._final_price = 0.0  # Final price after discount
        self._is_bulk_order = False  # Whether the order is a bulk order
        self._is_loyalty_discount_applied = False  # Flag to track loyalty discount application

    def get_order_id(self):
        # Return the order ID
        return self._order_id

    def set_order_id(self, order_id):
        # Set a new order ID
        self._order_id = order_id

    def get_order_date(self):
        # Return the order date
        return self._order_date

    def set_order_date(self, order_date):
        # Set a new order date
        self._order_date = order_date

    def get_customer(self):
        # Return the customer who placed the order
        return self._customer

    def set_customer(self, customer):
        # Set the customer for this order
        self._customer = customer

    def get_ebooks(self):
        # Return the list of e-books in the shopping cart
        return self._shopping_cart._itemsList

    def set_ebooks(self, ebooks):
        # Set the list of e-books in the shopping cart
        self._shopping_cart._itemsList = ebooks

    def get_invoice(self):
        # Return the invoice for the order
        return self._invoice

    def set_invoice(self, invoice):
        # Set the invoice for the order
        self._invoice = invoice

    def get_discount(self):
        # Return the discount applied to the order
        return self._discount_amount

    def set_discount_amount(self, discount_amount):
        # Set a new discount for the order
        self._discount_amount = discount_amount

    def get_final_price(self):
        # Return the final price after applying the discount
        return self._final_price

    def calculate_final_price(self):
        # Calculate the final price before any discount
        subtotal = sum(item._price for item in self._shopping_cart._itemsList)
        self._final_price = subtotal - self._discount_amount
        return self._final_price

    def apply_bulk_discount(self):
        # Apply a bulk discount if the customer orders more than 5 items
        if len(self._shopping_cart._itemsList) >= 5:
            self._discount_amount += 0.2 * self.calculate_final_price()  # 20% bulk discount
        return self._discount_amount

    def apply_loyalty_discount(self):
        # Check if the customer is a loyalty member and if the discount hasn't been applied yet
        if self._customer.is_loyalty_member and not self._is_loyalty_discount_applied:
            loyalty_discount = self._final_price * 0.10  # 10% loyalty discount
            self._final_price -= loyalty_discount
            self._is_loyalty_discount_applied = True
            self._discount_amount += loyalty_discount

    def is_bulk_order(self):
        # Return whether the order is a bulk order
        return self._is_bulk_order

    def set_bulk_order(self, status):
        # Set the status of whether the order is a bulk order
        self._is_bulk_order = status

    def __str__(self):
            # Return a string representation of the order details
         return f"Order(order_id={self._order_id}, order_date={self._order_date}, customer={self._customer}, " \
                f"ebooks={self._shopping_cart._itemsList}, discount_amount={self._discount_amount}, " \
                f"final_price={self._final_price})"

# Invoice class represents an invoice for an order, including charges, discounts, and total.
class Invoice:
    """Represents an invoice for an order, detailing the charges and discounts."""
    def __init__(self, invoice_number, order_items, subtotal, vat, discount, total):
        # Initialize invoice details, including the order items and total amount
        self._invoice_number = invoice_number
        self._order_items = order_items
        self._subtotal = subtotal
        self._vat = vat
        self._discount = discount
        self._total = total

    def display_invoice(self):
        # Display the invoice details
        print(f"Invoice Number: {self._invoice_number}")
        print(f"Items: {self._order_items}")
        print(f"Subtotal: {self._subtotal}")
        print(f"VAT: {self._vat}")
        print(f"Discount: {self._discount}")
        print(f"Total: {self._total}")

    def get_invoice_number(self):
        return self._invoice_number

    def set_invoice_number(self, invoice_number):
        self._invoice_number = invoice_number

    def get_order_items(self):
        return self._order_items

    def set_order_items(self, order_items):
        self._order_items = order_items

    def get_subtotal(self):
        return self._subtotal

    def set_subtotal(self, subtotal):
        self._subtotal = subtotal

    def get_vat(self):
        return self._vat

    def set_vat(self, vat):
        self._vat = vat

    def get_discount(self):
        return self._discount

    def set_discount(self, discount):
        self._discount = discount

    def get_total(self):
        return self._total

    def set_total(self, total):
        self._total = total

    def update_invoice(self, order):
        """Update the invoice with the current order details."""
        self._subtotal = sum(item._price for item in order._shopping_cart._itemsList)
        self._discount = order._discount_amount
        self._total = order._final_price
        # Assuming VAT is 8%, adjust as needed
        self._vat = 0.08 * self._subtotal
        self._total += self._vat

    def __str__(self):
        return f"Invoice(invoice_number={self._invoice_number}, total={self._total})"

 # Payment class represents the payment for an order.
class Payment:
        """Represents the payment for an order."""

        def __init__(self, payment_id, order, payment_method, amount_paid, payment_date):
            # Unique identifier for the payment transaction
            self._payment_id = payment_id
            # The order associated with this payment
            self._order = order
            # Payment method used (e.g., credit card, cash, etc.)
            self._payment_method = payment_method
            # Amount paid by the customer for the order
            self._amount_paid = amount_paid
            # Date on which the payment was made
            self._payment_date = payment_date

        def validate_payment(self):
            """Validate the payment amount against the order's total price."""
            # Checks if the amount paid is sufficient to cover the order's total
            if self._amount_paid >= self._order._final_price:
                return True
            return False

        def __str__(self):
            # Returns a string representation of the payment details
            return (f"Payment(payment_id={self._payment_id}, method={self._payment_method}, "
                    f"amount_paid={self._amount_paid}, date={self._payment_date})")

