from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import CharacterForms
from .models import Character


# Create your views here.
def index(request):
    # Grab all character names and print them
    latest_character_list = Character.objects.order_by('id')
    context = {'latest_character_list': latest_character_list}
    return render(request, 'rpgapp/index.html', context)
    # output = ', '.join([c.name for c in latest_character_list])
    # return HttpResponse(output)


def character_creation(request):
    if request.method == 'POST':
        form = CharacterForms(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            stamina = form.cleaned_data['stamina']
            perception = form.cleaned_data['perception']
            endurance = form.cleaned_data['endurance']
            charisma = form.cleaned_data['charisma']
            intelligence = form.cleaned_data['intelligence']
            agility = form.cleaned_data['agility']
            luck = form.cleaned_data['luck']
            character = Character(name=name, stamina=stamina, perception=perception, endurance=endurance, charisma=charisma, agility=agility, intelligence=intelligence, luck=luck)
            character.save()

            return HttpResponseRedirect(f'/rpgapp/{character.id}', {'character': character})
    else:
        form = CharacterForms()
        context = {'form': CharacterForms}
        return render(request, 'rpgapp/character_creation.html', context)


def character_page(request, character_id):
    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    return HttpResponse(f"<a href='/rpgapp'>Back</a>{character}")
