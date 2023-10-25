# TODO Найдите количество книг, которое можно разместить на дискете

disk_Mb = 1.44
symbol_b = 4

symbols = 25
lines = 50
pages = 100

book_b = symbol_b * symbols * lines * pages
book_mb = book_b / (1024)**2

amount_books = round(disk_Mb // book_mb)

print("Количество книг, помещающихся на дискету:", amount_books)
