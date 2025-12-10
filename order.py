class Order:
    orders = []

    def __init__(self, product, qty):
        self.product = product
        self.qty = qty
        Order.orders.append(self)

    def __str__(self):
        return f"{self.product.name} - Buyurtma soni {self.qty}"

