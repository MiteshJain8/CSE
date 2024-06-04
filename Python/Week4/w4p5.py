# Develop a python program to create a class called as "Invoice" with following attributes and methods. Declare and use the two arrays to hold items purchased, and price of the items. Write the calculateTax() method where GST tax is calculated. Write the printInvoice() function where the final bill is generated. Note: There are four types of items. Type 1 has 5% GST. Type 2 has 12% GST. Type 3 has 18% GST. Type 4 has 28% GST

class Invoice:
    def __init__(self, items, prices, types):
        self.items = items
        self.prices = prices
        self.types = types

    def total_tax(self):
        tot_tax = 0
        for i in range(len(self.prices)):
            if self.types[i] == 1:
                tot_tax += self.prices[i] * 0.05
            elif self.types[i] == 2:
                tot_tax += self.prices[i] * 0.12
            elif self.types[i] == 3:
                tot_tax += self.prices[i] * 0.18
            else:
                tot_tax += self.prices[i] * 0.28
        return tot_tax

    def print_invoice(self):
        print("Your Invoice is:")
        for i in range(len(self.items)):
            print(self.items[i], self.prices[i])
        print("Total Price:", sum(self.prices))
        print("Total Tax:", self.total_tax())
        print("Total After Tax:", sum(self.prices)+self.total_tax())

invoice = Invoice(["Pen", "Pencil", "Eraser"], [10, 20, 30],[3, 1, 4])
invoice.print_invoice()