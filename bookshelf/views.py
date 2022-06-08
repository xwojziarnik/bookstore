from django.shortcuts import render
from typing import List, Dict, Any
import requests
from django.utils.dateparse import parse_date
from requests import RequestException, Response
from .models import Book
from rest_framework import generics

# Create your views here.


def download_books_from_api(request, query_arg):
    books = f"https://www.googleapis.com/books/v1/volumes?q={query_arg}"
    return render(request, template_name='test.html', {query_arg})


def get_books_from_google_api(query_arg: str = "hobbit") -> List[Book]:
    for i in range(0, _generate_total_items_number(), 40):
        queries = {"q": query_arg, "startIndex": str(i), "maxResults": "10"}
        books_volume_url = f"https://www.googleapis.com/books/v1/volumes"
        books: List[Book] = []

        try:
            google_response: Response = requests.get(books_volume_url, params=queries)
        except RequestException as e:
            print(f"Encountered error while requesting to google, more info: {e.args}")
            return []
        else:
            if google_response.status_code in range(200, 299):
                results: Dict[str, Any] = google_response.json()
                for item in results.get("items", []):
                    books.append(_build_book_from_item(item))
            else:
                print(f"Request of {google_response.url} has status {google_response.status_code}")
    return books    # type: ignore


def _build_book_from_item(item: Dict[str, Any]) -> Book:
    book_info: Dict[str, Any] = item["volumeInfo"]
    book = Book.objects.update_or_create(title=book_info.get("title"),
        authors = book_info.get("authors"),
        acquired=False,
        publication_date=parse_date(book_info.get("publishedDate", "")),
        thumbnail=book_info["imageLinks"]["thumbnail"] if book_info.get("imageLinks") else "",
    )[0]
    print(book)
    book.authors.set([author.id for author in authors])     # type: ignore
    return book


def _generate_total_items_number(query_arg: str = "hobbit") -> int:
    books_volume_url = f"https://www.googleapis.com/books/v1/volumes?q={query_arg}"
    google_response: Response = requests.get(books_volume_url)
    return google_response.json()["totalItems"]
