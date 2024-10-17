from Laptop import Laptop

class Macbook(Laptop):
    def __init__(self,name : str,price : float,chip : str ,quantity=1):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Assigning self object
        self.chip = chip

        # Actions to execute
        Macbook.laptops.append(self)