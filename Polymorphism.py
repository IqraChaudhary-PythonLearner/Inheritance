credit_card_list = []
paypal_list = []
wire_transfer_list = []
money_gram_list = []
x = 1
while x == 1:
    continue_or_not = input("Do you want to continue(y/n)?: ").lower()
    if continue_or_not == "y":
        class PaymentSystem():
            def process_payment(self, amount):
                pass
            
        payment_method = int(input("""Choose a payment method:
1) Credit Card
2) PayPal
3) Wire Transfer
4) Money Gram
>>> """))
        class CreditCard(PaymentSystem):
            def process_payment(self):
                amount = int(input("Enter any amount: $"))
                credit_card_list.append(amount)
                print(f"Processing credit card payment of ${amount}")
        class PayPal(PaymentSystem):
            def process_payment(self):
                amount = int(input("Enter any amount: $"))
                paypal_list.append(amount)
                print(f"Processing PayPal payment of ${amount}")
        class WireTransfer(PaymentSystem):
            def process_payment(self):
                amount = int(input("Enter any amount: $"))
                wire_transfer_list.append(amount)
                print(f"Processing Wire Transfer payment of ${amount}")
        class MoneyGram(PaymentSystem):
            def process_payment(self):
                amount = int(input("Enter any amount: $"))
                money_gram_list.append(amount)
                print(f"Processing Money Gram payment of ${amount}")
        if payment_method == 1:
            Customer1 = CreditCard()
            
        if payment_method == 2:
            Customer2 = PayPal()
            Customer2.process_payment()
        if payment_method == 3:
            Customer3 = WireTransfer()
            Customer3.process_payment()
        if payment_method == 4:
            Customer4 = MoneyGram()
            Customer4.process_payment()
        print("Credit Card Payments:")
        for payments in credit_card_list:
            print("$",payments, end=" ")

        print("\nPayPal Payments:")
        for payments in paypal_list:
            print("$",payments, end=" ")

        print("\nWire Transfer Payments:")
        for payments in wire_transfer_list:
            print("$",payments, end=" ")

        print("\nMoney Gram Payments:")
        for payments in money_gram_list:
            print("$",payments, end=" \n")
    else:
        print(f"A total of ${sum(credit_card_list)} was transferred to your Credit Card.")
        print(f"A total of ${sum(paypal_list)} was transferred to your PayPal account.")
        print(f"A total of ${sum(wire_transfer_list)} was transferred to your Wire Transfer account.")
        print(f"A total of ${sum(money_gram_list)} was transferred to your Money Gram account.")
        print("Okay, Bye!")
        quit()