from django.contrib import admin
from room.models import Room, Character

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'game_type', 'image_img',)


class ImageAdmin_item(admin.ModelAdmin):
    list_display = ( 'name', 'race', 'image_img', )
   # list_filter = ( 'room', )


admin.site.register( Room, ImageAdmin )
admin.site.register(  Character,  ImageAdmin_item)
# admin.site.register()
admin.site.site_header = "Fight-Club Adminka"
