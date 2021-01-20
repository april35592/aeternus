from django.contrib import admin
from .models import Guest, Reply
# Register your models here.

class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 1

class GuestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'content']}),
        ('Date', {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [ReplyInline]
    search_fields = ['name']

admin.site.register(Guest, GuestAdmin)
