from django.contrib import admin

from .models import Group


# регистрируем модель групп в админке, чтобы создавать их
admin.site.register(Group)
