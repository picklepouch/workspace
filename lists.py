import time
booklist = [
    "Leviathan - Thomas Hobbes",
    "The Communist Manifest - Karl Marx",
    "Antichrist - Nietzche",
    
]
for book in booklist:
    print(book)
    time.sleep(.5)
new_book = input("Add a book to the booklist?  ")
while new_book.lower() == "yes":
    book = input("What book?  ")
    booklist.append(book)
    new_book = input("Add another?  ")

if new_book.lower == "no":
    for book in booklist:
        print(book)
        time.sleep(.5)