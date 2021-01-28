from django.contrib import admin
from tinymce.widgets import TinyMCE
from .models import Tutorials, TutorialSeries, TutorialCategory
from django.db import models
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fieldsets =[
    ("Title/date",{"fields":["tutorial_title", "tutorial_published"]}),
    ("URL",{"fields":["tutorial_slug"]})
    ("Series",{"fields":["tutorial_series"]})
    ("content",{"fields":["tutorial_content"]})

    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
     }
admin.site.register(Tutorials, TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
