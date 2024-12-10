class Products:
    def __init__(self):
        self.product = None
        self.price = None
        self.products_list = []
    def product_info(self):
        total = 0
        add_more = input("Do you want to add another product?(y/n): ")
        while add_more == "y":
            self.product = input("Enter another product name: ")
            self.price = int(input("Enter the product price: $"))
            total += self.price
            self.products_list.append(self.product)
            add_more2 = input("Do you want to add another product?(y/n): ").lower()
            if add_more2 == "y":
                continue
            elif add_more2 == "n":
                break
            else:
                print("Invalid Input")
                quit()
                break
        print(f"Your total balance is ${total}")
    def remove_item(self):
        item_to_remove = input("Enter the item you want to remove: ")
        self.products_list.remove(item_to_remove)
        if not self.products_list:
            print("Your cart is empty")
        else:    
            for items in self.products_list:
                print(items, end="\n")
        
product1 = Products()
product1.product_info()
product1.remove_item()
class Checkout:
    pass
