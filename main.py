def main():

    # String variable with the path to the Frankenstein book.
    book_path = "books/frankenstein.txt"

    # String variable that receives the whole content of the book.
    text = get_book_text(book_path)

    # Int variable that will store the total number of words in the book.
    num_words = get_num_words(text)

    # Dictionary variable that will store each character present on the book and their
    #  individual count.
    num_chars = get_char_count(text)
    
    # List variable receiving the conversion of the dictionary to a list.
    char_list = dict_to_list(num_chars)

    # Sorting of the list by char count.
    char_list.sort(reverse=True,key=sort_on)

    # Prints to console of the various variables above.
    print(text)
    print(num_words)
    print(num_chars)
    print(char_list)
    
    
# Function that converts the book text file into String.    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
# Function that counts the total number of words present in the book.
def get_num_words(text):    
    words = text.split()
    return len(words)

# Function that counts the amount of times each character appears in the book.
def get_char_count(text):
    lowered_text = text.lower()
    characters = {}
    for t in lowered_text:
        if (t in characters):
            characters[t] += 1
        else:
            characters[t] = 1
    
    return characters

# Function that converts a dictionary into a list.
def dict_to_list(dict):
    dlist = []
    for key, value in dict.items():
        if (key.isalpha()):
            dlist.append({"name": key, "num": value})
    return dlist


# Dictionary sorting function.
def sort_on(dict):
    return dict["num"]


main()