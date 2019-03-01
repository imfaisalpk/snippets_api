from django.contrib import admin
from snippets import models

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)


# Register your models here.
admin.site.register(models.Snippet, SnippetAdmin)