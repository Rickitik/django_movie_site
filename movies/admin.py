from django.contrib import admin
from .models import Categories, Genre, Movie, Actor, MovieShots, Reviews, Rating, RatingStar


admin.site.register(Categories)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)