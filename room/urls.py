from django.conf.urls import url, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
import mysite.urls

app_name = 'room'
urlpatterns = [
    url(r'^$', RoomListView.as_view(), name= "main"),
    #url(r'^$', show_room, name= "main"),
    url(r'^create/', create_players, name="create_players"),
   # url(r'^create_room/', create_room, name="create_room"),

   #  begin change Room #

    # ---OLD urls for functions = ROOM ----#
   #  url(r'^add_room/', add_room, name="add_room"),
    #url(r'^edit/(?P<pk>\d+)/$', edit, name='edit'),
    # url(r'^remove/(?P<pk>\d+)/$', remove, name='remove'),
    # ---OLD urls for functions = ROOM ----#

    # ---NEW urls for Class Base View = Room #
    url(r'^add_room/$', RoomCreateView.as_view(), name="add_room"),
    url(r'^edit/(?P<pk>\d+)/$', RoomUpdateView.as_view(), name='update_room'),
    url(r'^remove/(?P<pk>\d+)/$', RoomDeleteView.as_view(), name='remove_room'),
    url(r'^room_detail/(?P<pk>\d+)/$', RoomDetailView.as_view(), name='detail'),
    # ---NEW urls for Class Base View = Room #

    #  end change Room #

    # begin change Character #

    # ---OLD urls for functions = Character ----#
    #url(r'^add_character/', add_character, name="add_character"),
    # url(r'^edit_character/(?P<pk>\d+)/$', edit_character, name='edit_character'),
    # url(r'^remove_character/(?P<pk>\d+)/$', remove_character, name='remove_character'),
    # ---OLD urls for functions = Character ----#

    # ---NEW urls for Class Base View = Character #
    url(r'^add_character/', CharacterCreateView.as_view(), name="add_character"),
    url(r'^edit_character/(?P<pk>\d+)/$', CharacterUpdateView.as_view(), name='update_character'),
    url(r'^remove_character/(?P<pk>\d+)/$', CharacterDeleteView.as_view(), name='remove_character'),
    # ---NEW urls for Class Base View = Character #

    # end change Character #

    # url(r'^choose_character/(?P<pk><z>\d+)/$', edit_character, name='edit_character'),
    url(r'^enemy/$', choose_enemy, name="enemy"),
    url(r'^fight', fight_room, name="fight"),
    url(r'^attack/$', attack),
    url(r'^search/$', search),
    #url(r'^attack1/$', attack1, name="attack1"),
   # url(r'^apply/$', course_apply),
   # url(r'^create_room/$', show_rooms),
   # url(r'^/createplayers', create_players),

]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)