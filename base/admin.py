from django.contrib import admin

# Register your models here.


from .models import poetry,comments,category

admin.site.register(poetry)
admin.site.register(comments)
admin.site.register(category)
