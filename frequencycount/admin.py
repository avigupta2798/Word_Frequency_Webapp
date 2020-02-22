from django.contrib import admin
from frequencycount.models import WordCountUrl
# Register your models here.

class WordCountUrlAdmin(admin.ModelAdmin):
    search_fields = ['url']
    list_display = ['url']

admin.site.register(WordCountUrl, WordCountUrlAdmin)