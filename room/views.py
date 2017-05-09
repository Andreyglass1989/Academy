from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from room.models import Room, Character
from .character import Character_Demo
from django.views.decorators.csrf import csrf_protect
import random
from django.contrib import messages
from django import forms
from room.forms import RoomModelForm, CharacterModelForm
import datetime
from room.utils import detail_view
#CBV
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
#logging
import logging

logger = logging.getLogger(__name__)

player = Character_Demo("MAMBA","Ork")
enemy = Character_Demo("HEEEEH","Wolf")

# Create your views here.
# class ModelRoomAdd(forms.ModelForm):
#     class Meta:
#         model =  Room
#         exclude = ['data_begin', 'data_end', ]

class RoomListView(ListView):
    model = Room

    template_name = "main_menu.html"
    # context_object_name = "rooms"
    logger.debug("Room list!!")
    # def get_queryset(self):
    #     rooms = Room.objects.all()
    #     return rooms

    def get_context_data(self, **kwargs):
        context = super(RoomListView, self).get_context_data(**kwargs)
        rooms = Room.objects.all()
        context['title'] = "Rooms"
        context['rooms'] = rooms
        return context

# def show_room ( request ):   #show_room
#     # if request.method =="POST":
#     #     name_room = request.POST.get("nameRoom")
#     #     name_player = request.POST.get("nameChar")
#     #     name_race = request.POST.get("raceChar")
#     #     name_enemy = request.POST.get("nameEnem")
#     #     race_enemy = request.POST.get("raceEnem")
#     #     room = Room( name=name_room, game_type="SP" )
#     #     room.save()
#     #     players = Character( room=room, name = name_player, race = name_race )
#     #     enemy = Character( room=room, name=name_enemy, race=race_enemy )
#     #     players.save()
#     #     enemy.save()
#     rooms = Room.objects.all()
#     # characters = Character.objects.all()
#   #  print( rooms )
#     context = {
#         "title":"Rooms",
#         "rooms": rooms,
#         #"characters": characters,
#         #"model_form": model_form
#     }
#
#     return render(request, 'main_menu.html', context)

def create_players( request ):
   # races = []
   # for race in Character.RACE:
   #     races.append(race)
        #print(race)
    context = { "title": "Create players",
      "races": Character.RACE,}
      #"races": races }
    return render(request, "characters_create.html", context)


def choose_enemy(request):
    items = Enemy.objects.all()
    context = {
      "title": "Choose enemy",
      "items": items
    }
    return render(request, "Choose_enemy.html", context)


def fight_room( request ):
    context={ "title":"Fight room" }
    return render(request, "fight_room.html", context)


def attack ( request ):
   global player, enemy
   # enemy.health = 100
   # player.health = 100
   if request.is_ajax():
       while True:
           part_enemy = request.GET.get("partEnemy")
           part_player = request.GET.get("partPlayer")
           print(part_player)
           print(player.health)
           print(part_enemy)
           print(enemy.health)
           target=enemy.choice_target(random.randint(0,4))
           block=enemy.body_block(random.randint(0,4))
           print("enemy choice target = %s" %target)
           print("enemy block = %s" %block)

           player.choice_target(int(part_enemy))
           player.body_block(int(part_player))
           enemy.attack(player)
           player.attack(enemy)

           if enemy.body_block == 0:
               logger.debug("Block enemy Head")
               print("Block enemy Head")
           elif enemy.body_block == 1:
               logger.debug("Block enemy left hand")
               print("Block enemy left hand")
           elif enemy.body_block == 2:
               logger.debug("Block enemy torse")
               print("Block enemy torse")
           elif enemy.body_block == 3:
               logger.debug("Block enemy right hand")
               print("Block enemy right hand")
           elif enemy.body_block == 4:
               logger.debug("Block enemy foot")
               print("Block enemy foot")

           context = { "heathEnemy": enemy.health,
                       "healthPlayer": player.health,
                       }
           jsresp = JsonResponse(context)
           if enemy.health <= 0:
               print("Game over! You win!")
               logger.debug("Game over! You win!")
               messages.success(request, "Game over! You win!")
               print(jsresp.content)
               break
           elif player.health <=0:
               print("You lost! Game over!")
               logger.debug("You lost! Game over!")
               messages.success(request, "You lost! Game over!")
               print(jsresp.content)
               break
           print(jsresp.content)

       return render(request, 'fight_room.html')#HttpResponse(jsresp.content, content_type="text/html")
        #


# class RoomAddForm(forms.Form):
#     GAME_TYPES = (("SP", "Singleplay"), ("MP", "Multiplay"))
#     name = forms.CharField(max_length=50)
#     game_type = forms.ChoiceField( choices = (("SP", "Singleplay"), ("MP", "Multiplay")))
#     data_begin = forms.DateTimeField()
#     data_end = forms.DateField()
#     image = forms.ImageField()

# def detail(request, pk):
#     characters = Character.objects.all()
#     return detail_view(request, pk, Room, characters)


#----CBV for detail----#
class RoomDetailView(DetailView):
    model = Room
    context_object_name = "characters"
    template_name = "detail.html"

    def get_object(self, queryset=None):
        characters = Character.objects.all()
        return characters

#----CBV for detail----#

#----CBV for Room ----#

class RoomCreateView(CreateView):
    model = Room
    template_name = "add.html"
    form_class = RoomModelForm
    # fields = ['name', 'game_type', 'data_end', 'data_begin']
    # exclude = ['image']
    success_url = "/"

    def form_valid(self, form):
        response = super(RoomCreateView, self).form_valid(form)
        messages.success(self.request, "Room has been successfully added!")
        return response

class RoomUpdateView(UpdateView):
    model = Room
    template_name = "edit.html"
    form_class = RoomModelForm
    success_url = "/"

    def form_valid(self, form):
        response = super(RoomUpdateView, self).form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response

class RoomDeleteView(DeleteView):
    model = Room
    template_name = "remove.html"
    #form_class = RoomModelForm
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        response = super(RoomDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, "Room has been deleted.")
        return response

#----end CBV for Room ----#
# --BEGIN-- CHCANGE ROOM #

# def add_room(request):
#     if request.method == "POST":
#         print("method POST")
#         print(request.POST)
#         form = RoomModelForm(request.POST, request.FILES)
#         print("form= %s" %form)
#         if form.is_valid():
#             # print("form=%s" %form)
#             # data = form.cleaned_data
#             # print("data= %s" % data)
#             print("request.POST= %s" %request.POST)
#             print("request.POST= %s" % request.FILES)
#             room1 = Room()
#             room1.name = request.POST['name']
#             room1.game_type = request.POST['game_type']
#             room1.data_begin = request.POST['data_begin']
#             room1.data_end = request.POST['data_end']
#             # room1.image = request.FILES['image']
#             room1.save()
#             messages.success(request, "Room *%s* has been successfully added." % room1.name)
#             return redirect("/")
#         else:
#             print("none")
#     else:
#         print(request.GET)
#         print("method GET")
#         form = RoomModelForm(initial={'game_type': 'SP', 'data_begin': '2017-05-04', 'data_end': '2020-06-04'})
#         return render(request, 'add.html', {'form': form, 'title':'Room'})


# def edit(request, pk):
#     room = Room.objects.get(id=pk)
#     if request.method == "POST":
#         form = RoomModelForm(request.POST, instance=room)
#         print("form=%s" %form)
#         print(request.POST)
#         if form.is_valid():
#             room = form.save()
#             messages.success(request, "The changes have been saved.")
#             return redirect("/")
#     else:
#         form = RoomModelForm(instance=room)
#         return render(request, 'edit.html', {'form': form})
#
# def remove(request, pk):
#     room = Room.objects.get(id=pk)
#     if request.method == "POST":
#         room.delete()
#         messages.success(request, "Room %s has been deleted." % room.name)
#         return redirect("/")
#     else:
#         form = RoomModelForm(instance=room)
#     return render(request, 'remove.html', {'title': room})



# --END-- CHCANGE ROOM #


class CharacterCreateView(CreateView):
    model = Character
    template_name = "add.html"
    form_class = CharacterModelForm
    success_url = "/"

    def form_valid(self, form):
        response = super(CharacterCreateView, self).form_valid(form)
        messages.success(self.request, "Character has been successfully added!")
        return response

class CharacterUpdateView(UpdateView):
    model = Character
    template_name = "edit.html"
    form_class = CharacterModelForm
    success_url = "/"

    def form_valid(self, form):
        response = super(CharacterUpdateView, self).form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response

class CharacterDeleteView(DeleteView):
    model = Character
    template_name = "remove.html"
    # form_class = RoomModelForm
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        response = super(CharacterDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, "Character has been deleted.")
        return response

# --BEGIN-- CHCANGE Character #
# def add_character(request):
#     if request.method == "POST":
#         form = CharacterModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             charact = Character()
#             charact.name = request.POST['name']
#             charact.race = request.POST['race']
#             # charact.image = request.FILES['image']
#             charact.save()
#             messages.success(request, "Character *%s* has been successfully added." % charact.name)
#             return redirect("/")
#     else:
#         form = CharacterModelForm(initial={'race': 'HM'})
#         return render(request, 'add.html', {'form': form, 'title':'Character'})
#
# def edit_character(request, pk):
#     charact = Character.objects.get(id=pk)
#     if request.method == "POST":
#         form = CharacterModelForm(request.POST, instance=charact)
#         if form.is_valid():
#             charact = form.save()
#             messages.success(request, "The changes have been saved.")
#             return redirect("/")
#     else:
#         form = CharacterModelForm(instance=charact)
#         return render(request, 'edit.html', {'form': form, 'title': charact.name})
#
# def remove_character(request, pk):
#     charact = Character.objects.get(id=pk)
#     if request.method == "POST":
#         charact.delete()
#         messages.success(request, "Character %s has been deleted." % charact.name)
#         return redirect("/")
#     else:
#         form = CharacterModelForm(instance=charact)
#         return render(request, 'remove.html', {'title': charact})

# --END-- CHCANGE character #

@csrf_protect

def choose_enemy(request):
            items = Enemy.objects.all()
            context = {
                "title": "Choose enemy",
                "items": items
            }
            return render(request, "Choose_enemy.html", context)

    # def create_npc(name, race):
#     class Character:
#
#         damage = 25
#         health = 100
#         health_shield = 100
#         state = False
#
#         def __init__(self, name, race):
#             self.name = name
#             self.race = race
#
#         def hit(self, damage):
#             if self.state and (self.health_shield > 0):
#                 self.health_shield -= damage
#             else:
#                 self.health -= damage
#
#         def attack(self, enemy):
#             enemy.hit(self.damage)
#             if not enemy.state:
#                 self.damage += 10
#
#         def change_state(self, action):
#             if action == "attack":
#                 self.state = False
#             elif action == "shield":
#                 self.state = True