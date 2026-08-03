



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


c1 = Customer(4, "Hari", "hari@gmail.com", 9845226603)
c1.show_information()