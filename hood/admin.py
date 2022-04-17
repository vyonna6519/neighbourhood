from django.contrib import admin
from .models import neighbourhood,BlogPost,Profile


class HealthAdmin(admin.ModelAdmin):
    filter_horizontal =['healthservices']

# Register your models here.
admin.site.register(neighbourhood)
admin.site.register(BlogPost)
admin.site.register(Profile)


