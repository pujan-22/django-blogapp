
from django.contrib import admin

from app.models import Comments, Post, Tag, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Profile)