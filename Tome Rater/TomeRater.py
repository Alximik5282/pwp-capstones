class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def get_email(self):
        retrun self.email

    def change_email(self, address):
        self.email = address
        print("Email adress was changed!")

    def __repr__(self):
        return "User: {n}, email: {email}, books read: {number}".format(n = self.name, email = self.email, number = len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False
                
    def read_book(self, book, rating = None):
        self.books[book] = rating
    
    def get_average_rating(self):
        total = 0
        average = 0
        for values in self.books.values():
            if values.rating != None and len(self.books) != 0:
                total += values
                average = total / len(self.books)
        return average
                
class Book(object):
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.isbn = isbn
        print("Book's ISBN has been update!")
    
    def add_rating(self, rating):
        if rating > 0 and rating =< 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
        
    def __eq__(self, other_book):
        if self.title == other_book.title:
            if self.isbn == oyher_book.isbn:
                Book() = other_book
    
    def def get_average_rating(self):
        total = 0
        average = 0
        for ratings in self.ratings:
            total += ratings
            average = total / len(self.ratings)
        return average
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{t} by {a}".format(t = self.title, a = self.author)
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        self.title = super().self.title
        self.isbn = super().self.isbn
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{t}, a {l} on {s}".format(t = self.title, l = self.level, s = self.subject)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(title, isbn):
        new_book = Book(title, isbn)
        return new_book
    
    def create_novel(title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction
    
    def create_non_fiction(title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction
    
    def add_book_to_user(self, book, email, rating = None):
        user = self.users.get(email, None)
        if user == None:
            print("No user with email {}".format(email))
        else:
            user.read_book(book, rating)
            book.add_rating(rating)
            for keys in self.books.keys():
                if book not in keys:
                    self.books[book] = 0
                elif book in keys:
                    self.books[book] += 1
    
    def add_user(name, email, books = None):
        new_user = User(name, email)
        if books != None:
            for book in books:
                TomeRater.add_book_to_user(book, email)
                
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
            
    def print_users(self):
        for values in self.users.values():
            print(values)
            
    def most_read_book(self):
        book = Book()
        hight_par = 0
        for key, value in self.books.items():
            if hight_par < value:
                hight_par = value
                book = key
        return book
    
    def highest_rated_books(self):
        book = Book()
        hight_par = 0
        for keys in self.books.keys():
            if hight_par < book.get_average_rating(keys):
                hight_par = book.get_average_rating(keys)
                book = keys
        return book
    
    def most_positive_user(self):
        hight_rat = 0
        user = User()
        for values in self.users.values():
            if hight_rat < user.get_average_rating(values):
                hight_rat = user.get_average_rating(values)
                user = values
        return user
    
    def get_n_most_expensive_books(self, n):
        n = Book()
        for keys in self.books.keys():
            if n.price < keys.price:
                n = keys
        return n
    
    def get_worth_of_users(self, user_email):
        user = self.users[user_email]
        total = 0
        for book in user.books:
            total += book.price
        return total