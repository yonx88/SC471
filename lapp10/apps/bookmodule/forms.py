from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        widgets = {
            'title': forms.TextInput(),
            'author': forms.TextInput(),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'edition': forms.NumberInput(attrs={'min': 1}),
        }

        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'price': 'Price',
            'edition': 'Edition Number',
        }
