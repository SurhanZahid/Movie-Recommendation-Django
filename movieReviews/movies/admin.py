from django.contrib import admin
from .models import Movies,Ratings
# Register your models here.

class MovieAdmin(admin.ModelAdmin):

    search_fields = ['title', 'genres',]
    list_display = ["title","genres"]
    class Meta:
        model = Movies

class RatingAdmin(admin.ModelAdmin):

    list_display = ["userId","movieId","rating",]
    class Meta:
        model = Ratings

admin.site.register(Movies,MovieAdmin)
admin.site.register(Ratings,RatingAdmin)