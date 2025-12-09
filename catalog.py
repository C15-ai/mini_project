class Catalog:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        if isinstance(product, Store):
            self.products.append(product)
    def get_list(self):
        return self.products

    def search(self,name):
        for i in self.products:
            if i.name.lower()==name.lower():
                return i
            return None

