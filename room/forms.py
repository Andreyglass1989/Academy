from django import forms
from django.forms import ModelForm
from room.models import Room, Character

class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'game_type',  'image']
        exclude = ['data_begin', 'data_end',]

class CharacterModelForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'image']
