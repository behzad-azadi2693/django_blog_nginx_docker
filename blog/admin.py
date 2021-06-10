from django.contrib import admin
from .models import Post
from django.http import HttpResponse
from django.core import serializers
# Register your models here.


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type = 'application/json')
    serializers.serialize('json', queryset, stream=response)
    return response
export_as_json.short_description = 'Export to json'


def make_publish(modeladmin, request, queryset):
    result=queryset.update(status='published')
    if result == 1:
        message_bit = '1 post changed'
    else:
        message_bit = f'{result} posts changed'
    modeladmin.message_user(request, f'{message_bit} successfully change to publish')
make_publish.short_description = 'change object status to publish'

def make_draft(modeladmin, request, queryset):
    result = queryset.update(status='draft')
    if result == 1:
        message_bit = '1 post changed'
    else:
        message_bit = f'{result} posts changed'
    modeladmin.message_user(request, f'{message_bit} successfully change to draft')
make_draft.short_description = 'change object status to draft'


class PostAdmin(admin.ModelAdmin):
    list_display = ('titlle', 'publish', 'status')
    prepopulated_fields = {'slug':('titlle',)}
    list_filter = ('titlle', 'publish', 'status')
    search_fields = ('titlle', 'body')
    ordering = ('status', 'publish')
    actions = [make_publish, make_draft,export_as_json]

admin.site.register(Post, PostAdmin)