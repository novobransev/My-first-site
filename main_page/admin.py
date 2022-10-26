from django.contrib import admin
from .models import InfoImg, Homework, DateNow, Title_eveen_week, Title_odd_week, Border_odd_week, Border_even_week, Desc

admin.site.register(InfoImg)
admin.site.register(Homework)
admin.site.register(DateNow)
admin.site.register(Border_even_week)
admin.site.register(Border_odd_week)
admin.site.register(Title_eveen_week)
admin.site.register(Title_odd_week)
admin.site.register(Desc)