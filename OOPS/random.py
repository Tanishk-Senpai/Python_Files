class Person:
    def __init__(self, name: str, age: int):
        assert age > 0

        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Worker(Person):
    def __init__(self, name: str, age: int, profession : str, salary: int):
        super().__init__(name, age)

        assert salary > 0
        assert age >= 18

        self.profession = profession
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12
'''
worker1 = Worker('tanishk', 18, profession='SWE', salary=100 )
print(worker1.calc_yearly_salary())
person1 = Person('tanishk', 17)
print(person1)
print(person1.__repr__())
'''
class Book:
    def __init__(self, title: str, author: str, price: int):
        assert price > 0

        self._title = title
        self._author = author
        self._price = price

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Price: {self._price}"

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def price(self):
        return self._price

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @price.setter
    def price(self, new_price):
        self._price = new_price

    def apply_discount(self, discount_percentage: int):
        if 0 < discount_percentage <= 100:
            self._price -= self._price * discount_percentage / 100
            return self._price
        else:
            return "Invalid Discount"

book1 = Book('1984', 'George Orwell', 100)
print(book1)

print(book1.apply_discount(20))
print(book1._price)

book1._price = 200
print(book1)

numbers = [1, 2, 3, 4, 5]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

