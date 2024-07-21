from django.contrib import admin
from . import models



admin.site.register(models.Category)
admin.site.register(models.Cook)
admin.site.register(models.Banner)
admin.site.register(models.Meal)
admin.site.register(models.AboutUs)
admin.site.register(models.Comment)
admin.site.register(models.Reserve)