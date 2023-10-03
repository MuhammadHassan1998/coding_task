from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Book, Collaboration, Section


class SectionAdmin(DjangoMpttAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )


class CollaborationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "book",
        "is_author",
    )


admin.site.register(Section, SectionAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Collaboration, CollaborationAdmin)
