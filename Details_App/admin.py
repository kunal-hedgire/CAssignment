from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Author)
admin.site.register(Book)
