from Book import Book

Book1 = Book("zamalik", "ali", "9780743273565", True)
Book2 = Book("ahliy", "omar", "9780451524935", False)
print(f"Title: {Book1.title}, Author: {Book1.author}, ISBN: {Book1.isbn}, Available: {Book1.is_available}")
print(f"Title: {Book2.title}, Author: {Book2.author}, ISBN: {Book2.isbn}, Available: {Book2.is_available}")