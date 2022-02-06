from django.contrib import admin
from .models import Category, Movie, TvShow
#esto es para impprtar los modelos para el panel de admin
#MAS INFORMACION EN /PAGES/ADMIN

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')#con el __ accedemos a una propiedad que esta relacionada al modelo-
    list_display = ('title', 'user', 'created_at', 'public')
    list_filter = ('public', 'user__username', 'categories__name' )

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

class TvShowAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')#con el __ accedemos a una propiedad que esta relacionada al modelo-
    list_display = ('title', 'user', 'created_at', 'public')
    list_filter = ('public', 'user__username', 'categories__name' )

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(TvShow, TvShowAdmin)



