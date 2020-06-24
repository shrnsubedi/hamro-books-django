from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator

# Book genre choices
BOOK_CHOICES = (
    ("None", "None"),
    ("Fiction", "Fiction"),
    ("Non-fiction", "Non-fiction"),
    ("Biography", "Biography"),
    ("Other", "Other"),
)

BOOK_CONDITION = (
    ("New", "New"),
    ("Used", "Used"),
    ("Fine", "Fine"),
    ("Torn", "Torn"),
)

# Create your models here.
class Book(models.Model):
    # details about the book itself
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(9999999999)]
    )
    description = models.TextField(null=True)
    published = models.DateField(auto_now_add=False)
    image = models.ImageField(upload_to="books")
    genre = models.CharField(max_length=50, choices=BOOK_CHOICES, default="None")
    # details about the book ad
    book_condition = models.CharField(
        max_length=50, choices=BOOK_CONDITION, default="Used"
    )
    posted = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])

    # If image is present use return the url to template, else use placeholder
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = "static/placeholder.jpg"
        return url


class Speak(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="speaks")
    speak = models.CharField(max_length=250)
    posted = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.speak

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.book.id)])

