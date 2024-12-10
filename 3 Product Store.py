class ShoppingMart:
    def __init__(self):
        self.products1 = None
        self.products2 = None
        self.price1 = 15
        self.price2 = 37
        self.price3 = 8
        self.total_price = []
        self.total_products = []
    def display_choose_products(self):
        products = print("""Enter a Product Number(1, 2, or 3)
1. Soccer Ball: $15
2. Singing Microphone: $37
3. Ponds Facewash: $8""")
        product1 = int(input(">>> "))
        
        if product1 > 3 or product1 <= 0:
            print("Invalid Input. (For product 1)")
        continue_or_not = input("Do you want to try again?(y/n): ").lower()
        if continue_or_not == "y":
            product2 = int(input(">>> "))
        if product2 > 3 or product2 <= 0:
            print("Invalid Input. (For product 2)")
        if product1 == 1 or product2 == 1:
            self.total_products.append("1. Soccer Ball: $15")
            self.total_price.append(15)
        if product1 == 2 or product2 == 2:
            self.total_products.append("2. Singing Microphone: $37")
            self.total_price.append(37)
        if product1 == 3 or product2 == 3:
            self.total_products.append("3. Ponds Facewash: $8")
            self.total_price.append(8)
        print("SHOPPING CART")
        for items in self.total_products:
            print(items, end="\n")
        print(f"Currrently the total price ${(sum(self.total_price))}")
    def remove_item(self):
        remove_item = int(input("Enter a product number to remove: "))
        if remove_item == 1:
            if "1. Soccer Ball: $15" not in self.total_products:
                print("Item has not been purchased")
            self.total_products.remove("1. Soccer Ball: $15")
            self.total_price.remove(15)
        if remove_item == 2:
            if "2. Singing Microphone: $37" not in self.total_products:
                print("Item has not been purchased")
            self.total_products.remove("2. Singing Microphone: $37")
            self.total_price.remove(37)
        if remove_item == 3:
            if "3. Ponds Facewash: $8" not in self.total_products:
                print("Item has not been purchased")

            self.total_products.remove("3. Ponds Facewash: $8")
            self.total_price.remove(8)
        
        for items in self.total_products:
                print(items, end="\n")

FirstCustomer = ShoppingMart()
FirstCustomer.display_choose_products()
FirstCustomer.remove_item()