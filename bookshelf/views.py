
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
from urllib3 import response


def testing_view(request):
    """
    Testing function to understand how to implement class below.
    """
    if response.method == "POST":
        query_arg = response.POST.get("query_arg")
    return render(request, template_name="books_import.html", context={"query_arg":query_arg})


class BooksImport(CreateView):
    """
    I want to implement function where I can write online a word which will be a query arg
    that will be added to url below:
    https://www.googleapis.com/books/v1/volumes?q=
    for get books that will:
    be downloaded into db,
    get parameter "acquired" = True;
    .. and then app will response how many books was imported into db.
    """
    template_name = "books_import.html"

    def get_url(self, query_arg):
        pass
