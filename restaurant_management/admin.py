from django.contrib import admin
from .models import About,Restaurant

admin.site.register(About)
admin.site.register(Restaurant)
admin.site.register(Chef)

@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ("name", "price","created_at")