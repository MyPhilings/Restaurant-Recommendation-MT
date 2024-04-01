from django import forms

class restaurantForm(forms.Form):
    restaurant_input = forms.CharField(label = '',
                                       widget=forms.TextInput(attrs={'placeholder': 'Where do you wanna look? (e.g. Makati, Taguig)', 'style': 'width: 650px; height: 50px; font-size: 20px; padding-left: 10px;'}))