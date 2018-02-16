import pytest
import requests

@pytest.fixture(scope="session")
def app_url():
    return "http://pulse-rest-testing.herokuapp.com/"

@pytest.fixture(scope="session")
def book(app_url):
    response = requests.post(app_url + "books/", data={"title": "Fedor Dostoevsky", "author": "author"})
    book = response.json()
    yield book
    # q = requests.delete(app_url + "books/{}/".format(book["id"]))
    # print(q.status_code)
#
# @pytest.fixture(scope="session")
# def book2(app_url):
#     resp = requests.put(app_url + "books/", data={"title": "Crime and Punishment", "author": "Fedor Dostoevsky"})
#     book2 = resp.json()
#     yield book2
#
# @pytest.fixture(scope="session")
# def dele(app_url):
#     q = requests.delete(app_url + "books/{}/".format(book["id"]))
#     dele = q.json()
#     yield q

@pytest.fixture(scope="session")
def role(book):
    return {"name": "Fedor", "level": 10, "type": "master", "book": book["id"]}

@pytest.fixture(scope="session")
def role2(book):
    return {"name": "Igor", "level": 10, "type": "student", "book": book["id"]}
