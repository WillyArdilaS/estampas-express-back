from django.contrib import admin
from apiPost.models import usuario
# Register your models here.


@admin.register(usuario)
class PostAdmin(admin.ModelAdmin):
    list_display: ['id', 'username']
