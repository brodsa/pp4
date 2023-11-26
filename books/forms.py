import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import Book, BookContribution

# placeholders for text fields
# comment field in BookContribution form
COMMENT_TXT1 = 'You can comment on the book.'
COMMENT_TXT2 = 'What did you like or not like?'
COMMENT_TXT3 = 'Was it ease to read?'
COMMENT_TXT4 = 'Did you have AHA or WOW moment?'
COMMENT_TXT5 = 'Share your thoughts with us!'
# location_hidden field in BookContribution form
LOCATION_TXT1 = 'Give the detailed description about the hidden place,'
LOCATION_TXT2 = 'i.e. gps coordinates.'
LOCATION_TXT3 = 'This will help the other user to find the book.'


class BookForm(forms.ModelForm):
    """ Form to register Book """
    class Meta:
        """ Define model, fields, widget and labels """
        model = Book
        fields = [
            'title',
            'author',
            'published_year',
            'language',
            'description',
            'image',
            'image_alt',
        ]

        widgets = {
            "description": forms.Textarea(attrs={"cols": 3, "rows": 3}),
        }

        labels = {
            'title': 'Title',
            'author': 'Author',
            'published_year': 'Published Year',
            'language': 'Language',
            'description': 'Description',
            'image': 'Cover Image',
            'image_alt': 'Describe cover image',
        }

    # def clean(self):
    #     year = self.cleaned_data["published_year"]
    #     current_year = datetime.datetime.now().year
    #     if year > int(current_year):
    #         raise ValidationError('Invalid year.')
    #     elif year < 1900:
    #         raise ValidationError('Invalid year, please contact us if needed.')
    #     else:
    #         return year


class BookContributionForm(forms.ModelForm):
    """ A class for Book Contribution Form to contribute """

    class Meta:
        """ Define model, fields, widget and labels """
        model = BookContribution
        fields = [
            'city',
            'location',
            'location_hidden',
            'comment',
        ]

        widgets = {
            "location_hidden": forms.Textarea(
                attrs={
                    "cols": 3, 
                    "rows": 3,
                    "placeholder": " ".join([
                        LOCATION_TXT1,
                        LOCATION_TXT2,
                        LOCATION_TXT3
                        ])
                    }),
            "comment": forms.Textarea(
                attrs={
                    "cols": 3,
                    "rows": 3,
                    "placeholder": " ".join([
                        COMMENT_TXT1,
                        COMMENT_TXT2,
                        COMMENT_TXT3,
                        COMMENT_TXT4]
                    )
                    }),
        }

        labels = {
            'city': 'City',
            'location': 'Where is the book?',
            'location_hidden': 'Describe the hidden place!',
            'comment': 'How did you like the book?'
        }