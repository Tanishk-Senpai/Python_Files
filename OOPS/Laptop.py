import csv

class Laptop:
    pay_rate = 0.8
    laptops = []
    def __init__(self,name : str,price : float,quantity=1):
        # Running Validations for parameters
        assert quantity >= 0
        assert type(quantity) == int , f"{quantity} is not an integer!"

        # Assigning self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Laptop.laptops.append(self)

    def total_cost(self):
        return self.price * self.quantity
    def apply_discount(self):
        return self.price * self.pay_rate
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})')"

    # Class Methods
    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv','r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

        for laptop in data:
            Laptop(
                name = laptop.get('name'),
                price = int(laptop.get('price')),
                quantity = int(laptop.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For e.g: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False