from django.contrib import admin
from . import models
from django.db.models import Q

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file')


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {
        'slug': ('title',)
    }


from django.contrib.admin import SimpleListFilter


class TypeFilter(SimpleListFilter):
    title = 'type'  # or use _('country') for translated title
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        types = set()
        for c in model_admin.model.objects.all():
            if c.type.parent == None:
                types.add(c.type)
            else:
                types.add(c.type.parent)
        return [(c.id, c.title) for c in types]

    def queryset(self, request, queryset):
        return queryset.filter(Q(type_id=self.value()) | Q(type__parent_id=self.value()))


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'level', 'type')
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_filter = (TypeFilter,)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'rating')


@admin.register(models.SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'url')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'message')


@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'bio')

    def has_add_permission(self, request, obj=None):
        from .models import Home
        if Home.objects.all():
            return False
        return True


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
