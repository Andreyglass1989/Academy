from __future__ import unicode_literals
from datetime import datetime
from django.db import models


# Create your models here.

class Room( models.Model ):
    GAME_TYPES = (("SP","Singleplay"),("MP","Multiplay"))
    name = models.CharField( max_length = 50 )
    game_type = models.CharField( max_length = 3, choices = GAME_TYPES, default="SP")
    data_begin = models.DateField( auto_now = True, null=True )
    data_end = models.DateField( blank = True, null=True )
    image = models.ImageField(upload_to='Room', )

    def __str__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(
                self.image.url)
        else:
            return '(No image)'

    image_img.short_description = 'Picture'
    image_img.allow_tags = True



class Character( models.Model ):
    RACE = (("HM","Human"),("EL","Elf"),("OW","Orc"),("DW","Dwarf"),("WW","WareWolf"))
    # room = models.ForeignKey(Room)
    name = models.CharField(max_length=50)
    BODY_PARTS = ["Head", "Torso", "Left hand", "Right hand", "Lags"]
    race = models.CharField(max_length=3, choices=RACE)
    image = models.ImageField(upload_to='Character' )

    def __unicode__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" height="100"/></a>'.format(
                self.image.url)
        else:
            return '(No image)'

    image_img.short_description = 'Picture'
    image_img.allow_tags = True

    health = 100

    def __str__(self):
        return self.name

    def hit(self, target):
        if target == 0:
            self.health -= 50
        elif target == 1:
            self.health -= 40
        elif 2 <= target <= 3:
            self.health -= 10
        elif target == 4:
            self.health -= 20

    def attack(self, enemy):
        print(enemy.block_part)
        if self.target != enemy.block_part:
            enemy.hit(self.target)

    def choice_target(self, target):
        self.target = target

    def body_block(self, block_part):
        self.block_part = block_part





# class Enemy( models.Model ):
#     RACE = (("HM", "Human"), ("EL", "Elf"), ("OW", "Orc"), ("DW", "Dwarf"), ("WW", "WareWolf"))
#     name = models.CharField( max_length = 50 )
#     race = models.CharField(max_length=3, choices=RACE)
#     # room = models.ForeignKey(Room)
#     image = models.ImageField(upload_to = 'Enemy',)
#     def __unicode__(self):
#         return self.name
#
#     def image_img(self):
#         if self.image:
#             return u'<a href="{0}" target="_blank"><img src="{0}" width="100", height="200"/></a>'.format(self.image.url)
#         else:
#             return '(No image)'
#
#     image_img.short_description = 'Picture'
#     image_img.allow_tags = True



