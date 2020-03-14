from django.contrib import admin
from .models import RoomType,Purpose,Location,Room

# Register your models here.
admin.site.register(RoomType)
admin.site.register(Purpose)
admin.site.register(Location)
admin.site.register(Room)