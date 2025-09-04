from django.contrib import admin
from .models import About

admin.site.register(About)
admin.site.register(restaurant)

@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ("name", "price","created_at")