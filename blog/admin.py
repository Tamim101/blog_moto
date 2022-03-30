from django.contrib import admin

# Register your models here.
from blog.models import Room, User

admin.site.register(Room)
admin.site.register(User)