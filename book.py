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

    
       
    most_appearances= []
    name_and_frequency = {"name": '', "frequency": 0}
    book_names = set([book.name for book in book_list])
    for name in book_names:
        unique_names = list(filter(lambda book : book.name == name, book_list))
        unique_name_count = len(unique_names)

        if unique_name_count >= name_and_frequency["frequency"]:
            name_and_frequency["name"] = name 
            name_and_frequency["frequency"] = unique_name_count

    print(name_and_frequency)