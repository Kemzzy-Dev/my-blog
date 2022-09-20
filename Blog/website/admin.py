from django.contrib import admin
from .models import *

# Register your models here.

# Instead of model admin we use summernotemodeladmin in other to add the text editor to our article data 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'category','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}
    #Adding summernotes to our article data only
    # summernote_fields = 'article'


admin.site.register(post, PostAdmin)
admin.site.register(newsletter)
admin.site.register(contact)
admin.site.register(tag)
