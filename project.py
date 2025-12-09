from abc import ABC, abstractmethod


class Store(ABC):
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    @abstractmethod
    def info(self):
        pass

    def __str__(self):
        return f"Nomi: {self.name} Narxi: {self.price} Soni{self.qty}"


class Product(Store):
    def info(self):
        return f"{self.name} - {self.price}som - omborda {self.qty}"
