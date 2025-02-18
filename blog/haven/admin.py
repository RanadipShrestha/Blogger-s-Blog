from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(FAQ)
admin.site.register(Categories)
admin.site.register(Article)
admin.site.register(Feedback)
admin.site.register(Comment)