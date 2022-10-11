# TODO: Create a Book class with the following instance variables:
# name
# author
# user_rating
# number_of_reviews
# price
# year
# genre
#from unicodedata import name


class Book:

    def __init__(self,book_data_dictionary):
        self.name = book_data_dictionary["name"]
        self.author = book_data_dictionary["author"] 
        self.user_rating = book_data_dictionary["user_rating"]
        self.number_of_reviews = book_data_dictionary["number_of_reviews"]
        self.price = book_data_dictionary["price"]
        self.year = book_data_dictionary["year"]
        self.genre = book_data_dictionary["genre"]

    
       
    