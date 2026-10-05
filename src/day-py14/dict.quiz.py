def main():
    book = get_book_info()
    action = input("Do you want to (check out) or (return) the book: ")
    if action == "check out":
        check_out_book(book)
    elif action == "return":
        return_book(book)

    print(book)

def get_book_info():
    title = input("Enter title of the book: ")
    author = input("Enter author of the book: ")
    year = int(input("Enter the year the book was published: "))
    available = input("Available (True/False): ")

    if available == "True":
        available = True
    else:
        available = False


    return {"title": title,
            "author": author,
            "year": year,
            "available": available}


def check_out_book(book):
    if book["available"] == True:
        book["available"] = False
        print("Checked out succesfully")
    else:
        print("Sorry, this book is already checked out")
    return book
def return_book(book):
    book["available"] = True
    print("Book returned. Thank you!")
    return book
    


if __name__ =="__main__":
    main()


""" 
KEY LESSONS:
Use the parameter, don't recreate it - Inside check_out_book(book), use the book variable passed in

Access dictionary values with keys - Use book["available"] not just available """




