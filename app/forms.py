from django import forms
from .models import BuyModel, ContactModel

from .models import ProductModel


class BuyForm(forms.ModelForm):
    class Meta:
        model = BuyModel
        fields = ['full_name', 'email', 'phone', 'date', 'tour']

    def __init__(self, *args, **kwargs):
        tour_title = kwargs.pop('tour_title', None)
        start_date = kwargs.pop('start_date', None)
        super(BuyForm, self).__init__(*args, **kwargs)
        if tour_title:
            self.fields['tour'].initial = tour_title
        if start_date:
            self.fields['date'].initial = start_date


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

