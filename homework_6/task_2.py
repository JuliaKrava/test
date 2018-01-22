import requests

books_data = {
        "id": 25,
        "title": "Homework",
        "author": "Julia"
}

books_data2 = {
        "title": "Homework 6",
        "author": "Julia Kravchuk"
}

r = requests.post("http://pulse-rest-testing.herokuapp.com/books/", data=books_data)
books = r.json()
r1 = requests.put("http://pulse-rest-testing.herokuapp.com/books/35/", data=books_data2)
books2 = r1.json()
r2 = requests.delete("http://pulse-rest-testing.herokuapp.com/books/35/")
books3 = r2.json()
print(books3)
