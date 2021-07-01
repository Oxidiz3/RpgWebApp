import django.forms as forms

from rpgapp.models import Character


class CharacterForms(forms.Form):
    name = forms.CharField(label="Name\n", max_length=80)
    stamina = forms.CharField(label="Stamina\n", max_length=80)
    perception = forms.CharField(label="Perception\n", max_length=80)
    endurance = forms.CharField(label="Endurance\n", max_length=80)
    charisma = forms.CharField(label="Charisma\n", max_length=80)
    intelligence = forms.CharField(label="Intelligence\n", max_length=80)
    agility = forms.CharField(label="Agility\n", max_length=80)
    luck = forms.CharField(label="Luck\n", max_length=80)
