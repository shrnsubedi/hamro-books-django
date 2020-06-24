from django.contrib import admin
from .models import Book, Speak


# This allows to see associated comments in the Ad in the admin panel
class CommentInline(admin.StackedInline):
    model = Speak
    extra = 0


class BookAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Speak)
