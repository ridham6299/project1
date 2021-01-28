from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Tutorials
from django.db import models
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fieldsets =[
    ("Title/date",{"fields":["tutorial_title", "tutorial_published"]}),
    ("content",{"fields":["tutorial_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
     }
admin.site.register(Tutorials, TutorialAdmin)
