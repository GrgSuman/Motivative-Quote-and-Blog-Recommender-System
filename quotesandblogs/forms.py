from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
  class Meta:
    model=Contact
    fields=('full_name','email','phone','message')
    widgets={
      'full_name':forms.TextInput(attrs={'placeholder':"Name","autocomplete":"off"}),
      'email':forms.TextInput(attrs={'placeholder':"Email","autocomplete":"off"}),
      'phone':forms.TextInput(attrs={'placeholder':"Phone","autocomplete":"off"}),
      'message':forms.Textarea(attrs={'placeholder':"Enter  your message here","resize":"none"})
    }

    labels={
      'full_name':"",
      'email':'',
      'phone':"",
      'message':""
    }