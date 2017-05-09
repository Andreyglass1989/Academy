from django import forms
from django.forms import ModelForm
from room.models import Room, Character

class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'game_type', 'data_end', 'data_begin']
        exclude = ['image']

class CharacterModelForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race',]
        exclude = ['image']
