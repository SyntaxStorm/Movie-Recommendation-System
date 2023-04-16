from django.contrib import admin

from apps.feedback.models import FavoriteFilm, Like, Rating
from apps.films.models import Film, Tag, WatchedFilm

# Register your models here.

admin.site.register(Film)
admin.site.register(Like)
admin.site.register(FavoriteFilm)
admin.site.register(Tag)
admin.site.register(WatchedFilm)
admin.site.register(Rating)
