from data import data_list
from book import Book


def run_analysis(book_list):
    books = create_book_list(book_list)
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)


def create_book_list(data_list):
    book_list = []
        #TODO: Write a function that will loop through data_list, and create a Book object for each list item
        #TODO: Then, add each Book item to book_list
        #TODO: Finally, return book_list for use in analysis questions!
    for book in data_list:
        books_in_list = Book(book)
        book_list.append(books_in_list)


    return book_list


def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book.year == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book.price)
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book.name} with a price of {highest_cost_book.price}")


def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    books_2018 = list(filter(lambda book: book.year == 2018, book_list))
    lowest_num_review = min(book_list, key=lambda book:  book.number_of_reviews)
    print(f"The book with the lowest number of reviews in 2018 was {lowest_num_review}")

def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    non_fiction_list = list(filter(lambda book: book.genre == "Non Fiction", book_list))
    non_fiction_count = len(non_fiction_list)
    print(f"The total amount of non fiction books is {non_fiction_count}.")

    fiction_list = list(filter( lambda book : book.genre == "Fiction", book_list ))
    fiction_count = len(fiction_list)
    print(f"The total amount of fiction books is {fiction_count}.")
    print(f"The genre with the highest appearence count on the top 50's list is {non_fiction_count}!")
  
      
def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")
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
       
# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)
