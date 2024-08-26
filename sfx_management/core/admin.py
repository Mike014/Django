from django.contrib import admin
from .models import Category, Game, SoundEffect

# Register your models here.
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(SoundEffect)

