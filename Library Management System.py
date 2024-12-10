print("Library Management System")
class Library:
    def __init__(self):
        self.registered_users = ["Iqra", "Asmaa", "Amina"]
        self.borrowed_books = []
        self.returned_books = []
        #self.books = ["Ivy and Bean", "Fish in a Tree", "Peter Pan", "Geronimo Stilton"]
    def borrow_books(self):
        username = input("Enter your name: ")
        if username in self.registered_users:
            x = 1
            while x == 1:    
                    add_more = input("Do you want to borrow a book?(y/n): ").lower()
                    if add_more == "y":
                        options = int(input("""Choose a book from 1-4: 
1) Ivy and Bean
2) Fish in a Tree
3) Peter Pan
4) Geronimo Stilton
>>> """))
                        if options == 1:
                            if 1 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 1 not in self.borrowed_books:
                                self.borrowed_books.append(1)
                                
                        elif options == 2:
                            if 2 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 2 not in self.borrowed_books:
                                self.borrowed_books.append(2)

                        elif options == 3:
                            if 3 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 3 not in self.borrowed_books:
                                self.borrowed_books.append(3)

                        elif options == 4:
                            if 4 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 4 not in self.borrowed_books:
                                self.borrowed_books.append(4)

                        elif len(self.borrowed_books) == 4:
                            print("Sorry, your cart is full. Come again another time.") 
                        else:
                            print("That book is not available.")
                    elif add_more == "n":
                        Library.return_books(self)
                    else:
                        print("Invalid Input.")
        else:
            print("Your name is not registered")
            register_or_no = input("Do you want to register?(y/n): ").lower()
            if register_or_no == "y":
                name = input("""Enter your name to register below: 
>>> """)
                self.registered_users.append(name)
                x = 1
                while x == 1:    
                    add_more = input("Do you want to borrow a book?(y/n): ").lower()
                    if add_more == "y":
                        options = int(input("""Choose a book from 1-4: 
1) Ivy and Bean
2) Fish in a Tree
3) Peter Pan
4) Geronimo Stilton
>>> """))
                        if options == 1:
                            if 1 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 1 not in self.borrowed_books:
                                self.borrowed_books.append(1)
                                
                        elif options == 2:
                            if 2 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 2 not in self.borrowed_books:
                                self.borrowed_books.append(2)

                        elif options == 3:
                            if 3 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 3 not in self.borrowed_books:
                                self.borrowed_books.append(3)

                        elif options == 4:
                            if 4 in self.borrowed_books:
                                print("You already borrowed this book.")
                            elif 4 not in self.borrowed_books:
                                self.borrowed_books.append(4)

                        elif len(self.borrowed_books) == 4:
                            print("Sorry, your cart is full. Come again another time.") 
                        else:
                            print("That book is not available.")
                    elif add_more == "n":
                        Library.return_books(self)
                    else:
                        print("Invalid Input.")
        
            else:
                print("Sorry, no registeration NO BOOKS!")
                quit()
    def return_books(self):
        return_any = input("Do you want to return any book?(y/n): ").lower()
        if return_any == "y":
            book_to_return = int(input("Which book do you want to return?: "))
            if book_to_return in self.borrowed_books:
                self.returned_books.append(book_to_return)
                self.borrowed_books.remove(book_to_return)
            elif book_to_return not in self.borrowed_books:
                print("You haven't borrowed this book.")
                borrow_or_not = input("Do you want to borrow this book?(y/n): ").lower()
                if borrow_or_not == "y":
                    self.borrowed_books.append(book_to_return)
                    return_or_no = input("Do you want to return this book?(y/n): ").lower()
                    if return_or_no == "y":
                        self.borrowed_books.remove(book_to_return)
                    else:
                        print(f"Okay, you have added Book Number {book_to_return} to your list.")
                else:
                    print("Okay")
        else:
            Library.view_details(self)
    def view_details(self):
        print("BORROWED BOOKS")
        print("-----------------------------")
        for the_books in self.borrowed_books:
            if the_books == 1:
                print("Ivy and Bean")
            if the_books == 2:
                print("Fish in a Tree")
            if the_books == 3:
                print("Peter Pan")
            if the_books == 4:
                print("Geronimo Stilton")
        print("RETURNED BOOKS")
        print("-----------------------------")
        for the_returns in self.returned_books:
            if the_returns == 1:
                print("Ivy and Bean")
            if the_returns == 2:
                print("Fish in a Tree")
            if the_returns == 3:
                print("Peter Pan")
            if the_returns == 4:
                print("Geronimo Stilton")
        if len(self.returned_books) == 0:
            print("You returned 0 books")
            
        quit()
Customer1 = Library()
Customer1.borrow_books()
Customer1.return_books()
Customer1.view_details()