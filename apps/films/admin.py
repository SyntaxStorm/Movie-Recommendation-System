from django.contrib import admin

from apps.feedback.models import FavoriteFilm, Like, Rating
from apps.films.models import Film, Tag, View

# Register your models here.

admin.site.register(Film)
admin.site.register(Like)
admin.site.register(FavoriteFilm)
admin.site.register(Tag)
admin.site.register(View)
admin.site.register(Rating)
