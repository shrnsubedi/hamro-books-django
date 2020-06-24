from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book, Speak

# Create your views here.
class BookListView(ListView):
    template_name = "book_list.html"
    queryset = Book.objects.all()
    paginate_by = 3


class BookFilterListView(ListView):
    template_name = "book_list.html"
    paginate_by = 3

    def get_queryset(self):
        if self.kwargs["genre"] == "All":
            return Book.objects.all()
        else:
            return Book.objects.filter(genre=self.kwargs["genre"])


class BookSearchListView(ListView):
    template_name = "book_list.html"
    paginate_by = 3

    def get_queryset(self):
        book_name = self.request.GET.get("search")
        return Book.objects.filter(name__icontains=book_name)


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = (
        "name",
        "author",
        "isbn",
        "description",
        "published",
        "image",
        "genre",
        "price",
        "book_condition",
    )
    template_name = "book_edit.html"
    login_url = "login"

    def test_func(self):
        obj = self.get_object()
        return obj.posted == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("book_list")
    login_url = "login"

    """ 
     The test_func method is used by UserPassesTestMixin for our logic. We need to override it.
     In this case we set the variable obj to the current object returned by the view using get_object().
     Then we say, if the author on the current object matches the current user on the webpage 
     (whoever is logged in and trying to make the change), then allow it. If false, an error will 
     automatically be thrown. 
     """

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "book_new.html"
    fields = (
        "name",
        "author",
        "isbn",
        "description",
        "published",
        "image",
        "genre",
        "price",
        "book_condition",
    )
    login_url = "login"
    # Set the Posted field automatically to the current logged in user rather than by selection through fields.
    def form_valid(self, form):
        form.instance.posted = self.request.user
        return super().form_valid(form)


class SpeakCreateView(LoginRequiredMixin, CreateView):
    model = Speak
    template_name = "speak_post.html"
    fields = ("speak",)
    login_url = "login"

    def form_valid(self, form):
        form.instance.posted = self.request.user
        form.instance.book = Book.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
