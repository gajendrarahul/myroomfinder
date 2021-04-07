from django import forms
from . models import Room,Owner

class AddRoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['owner']