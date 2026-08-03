



class Customer:
    def __init__(self, customer_id, customer_name, customer_email, customer_phone):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_phone = customer_phone

    def show_information(self):
        print("Customer Information")
        print("------------------------")
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer Email: {self.customer_email}")
        print(f"Customer Phone: {self.customer_phone}")


class Product:
    def __init__(self, product_id, product_name, product_price, stock_remaining):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.stock_remaining = stock_remaining

    def show_information(self):
        print("Product Information")
        print("-------------------------")
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Product Price: {self.product_price}")
        print(f"Product Stock Remaining: {self.stock_remaining}")


p1 = Product(5, "Keyboard", 2, 250, 3)
p1.show_information()