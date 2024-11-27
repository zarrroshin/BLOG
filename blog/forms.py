from django import forms
from django.core.validators import ValidationError

from blog.models import Message


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=5, label='Your Message', widget=forms.Textarea(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=5, label='Your Name')

    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2001),attrs={'class':'form-control'}))

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        # if 'a' in name:
        #     self.add_error('name','a can not be in name')
        if name == text:
            raise ValidationError('name and text are same', code='name_text')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError('a can not be in name', code='a_in_name')
        return name + 'reza '


#
# class MessagesForm(forms.Form):
#     title = forms.CharField(max_length=100,label='Title')
#     text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
#     email = forms.EmailField()

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Title', "style": 'max-width: 300px'}),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Message', "style": 'max-width: 300px'}),
            'email': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your email', "style": 'max-width: 50px'})

        }
