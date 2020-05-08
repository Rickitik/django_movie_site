from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Categories, Genre, Movie, Actor, MovieShots, Reviews, Rating, RatingStar


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'url')  # отображение полей в админ панеле
	list_display_links = ('name',)  # назначение ссылки на переход


class ReviewInline(admin.TabularInline):  # подготавливаем объекты, которые встанут inline  в другом классе
	model = Reviews  # подключаем модель
	extra = 1
	readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	"""Фильмы"""
	list_display = ("title", "category", "url", "draft")
	list_filter = ("category", "year")
	search_fields = ("title", "category__name")
	inlines = [ReviewInline]
	save_on_top = True
	save_as = True
	list_editable = ("draft",)
	readonly_fields = ("get_image",)
	fieldsets = (
		(None, {
			"fields": (("title", "tagline"),)
		}),
		(None, {
			"fields": ("description", ("poster", "get_image"))
		}),
		(None, {
			"fields": (("year", "world_premiere", "country"),)
		}),
		("Actors", {
			"classes": ("collapse",),
			"fields": (("actors", "directors", "genres", "category"),)
		}),
		(None, {
			"fields": (("budget", "fees_in_usa", "fess_in_world"),)
		}),
		("Options", {
			"fields": (("url", "draft"),)
		}),
	)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

	get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'parent', 'movie', 'id')
	readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	"""Жанры"""
	list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	"""Актеры"""
	list_display = ("name", "age", 'get_image')
	readonly_fields = ('get_image', )  # вывод изображение так же в развернутую форму

	def get_image(self, obj):  # метод для получения тега с изображением из урл
		return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

	get_image.short_description = 'Изображение'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
	"""Рейтинг"""
	list_display = ("star", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
	"""Кадры из фильма"""
	list_display = ("title", "movie", 'get_image')
	readonly_fields = ('get_image', )

	def get_image(self, obj):  # метод для получения тега с изображением из урл
		return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

	get_image.short_description = 'Изображение'


admin.site.register(RatingStar)

admin.site.site_title = 'Django Movie Site'
admin.site.site_header = 'Django Movie Site'
