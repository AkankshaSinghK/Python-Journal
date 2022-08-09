# discount class with constructor and methods to calculate discount
class Discount:
    def __init__(self, name, rate, quantity):
        self.name = name
        self.rate = rate
        self.quantity = quantity
        self.amount = self.rate * self.quantity
        self.discount = 0
        self.discount_amount = 0

    def calculate_discount(self):
        if self.amount > 100000:
            self.discount = 20
        elif self.amount > 50000 and self.amount <= 100000:
            self.discount = 10
        else:
            self.discount = 5
        self.discount_amount = self.amount * self.discount / 100
        return self.discount_amount


if __name__ == "__main__":
    name = input("Enter the name of the product: ")
    rate = int(input("Enter the rate of the product: "))
    quantity = int(input("Enter the quantity of the product: "))
    obj = Discount(name, rate, quantity)
    obj.calculate_discount()
    print("The discount amount is: ", obj.discount_amount)
